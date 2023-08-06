"""Ubiquiti mFi MPower device"""
from __future__ import annotations

import asyncio
from random import randrange
import ssl
import time

import aiohttp
from aiohttp import ClientResponse, ClientSession
from yarl import URL

from .entities import MPowerSensor, MPowerSwitch
from .exceptions import (
    CannotConnect,
    InvalidAuth,
    InvalidData,
    InvalidResponse,
)


class MPowerDevice:
    """mFi mPower device representation."""

    _host: str
    _url: URL
    _username: str
    _password: str
    _eu_model: bool
    _cache_time: float

    _cookie: str
    _session: bool
    _ssl: bool | ssl.SSLContext

    _updated: bool
    _authenticated: bool
    _time: float
    _data: dict

    def __init__(
        self,
        host: str,
        username: str,
        password: str,
        use_ssl: bool = False,
        verify_ssl: bool = False,
        eu_model: bool = False,
        cache_time: float = 0.0,
        session: ClientSession | None = None,
    ) -> None:
        """Initialize the device."""
        self._host = host
        self._url = URL(f"https://{host}" if use_ssl else f"http://{host}")
        self._username = username
        self._password = password
        self._eu_model = eu_model
        self._cache_time = cache_time

        self._cookie = "".join([str(randrange(9)) for i in range(32)])
        self._cookie = f"AIROS_SESSIONID={self._cookie}"

        if session is None:
            self.session = ClientSession()
            self._session = True
        else:
            self.session = session
            self._session = False

        if use_ssl:
            # NOTE: Ubiquiti mFi mPower Devices only support SSLv3 and TLSv1.0
            self._ssl = ssl.SSLContext(ssl.PROTOCOL_TLSv1)
            self._ssl.set_ciphers("AES256-SHA:AES128-SHA:SEED-SHA")
            self._ssl.load_default_certs()
            self._ssl.verify_mode = ssl.CERT_REQUIRED if verify_ssl else ssl.CERT_NONE
        else:
            self._ssl = False

        self._updated = False
        self._authenticated = False
        self._time = time.time()
        self._data = {}

    def __del__(self):
        """
        Delete the device.

        This closes the async session if necessary as proposed here:
          https://stackoverflow.com/a/67577364/13613140
        """
        if self._session:
            try:
                loop = asyncio.get_event_loop()
                if loop.is_running():
                    loop.create_task(self.session.close())
                else:
                    loop.run_until_complete(self.session.close())
            except Exception:  # pylint: disable=broad-except
                pass

    async def __aenter__(self):
        """Enter context manager scope."""
        await self.login()
        await self.update()
        return self

    async def __aexit__(self, *kwargs):
        """Leave context manager scope."""
        await self.logout()

    def __str__(self):
        """Represent this device as string."""
        name = __class__.__name__
        keys = ["hostname", "ip", "hwaddr", "model"]
        vals = ", ".join([f"{k}={getattr(self, k)}" for k in keys])
        return f"{name}({vals})"

    @property
    def url(self) -> URL:
        """Return device URL."""
        return self._url

    @property
    def host(self) -> str:
        """Return device host."""
        return self._host

    @property
    def eu_model(self) -> bool:
        """Return whether this device is a EU model with type F sockets."""
        return self._eu_model

    @property
    def manufacturer(self) -> str:
        """Return the device manufacturer."""
        return "Ubiquiti"

    async def request(
        self, method: str, url: str | URL, data: dict | None = None
    ) -> ClientResponse:
        """Session wrapper for general requests."""
        url = URL(url)
        if not url.is_absolute():
            url = self.url / str(url).lstrip("/")
        try:
            resp = await self.session.request(
                method=method,
                url=url,
                headers={"Cookie": self._cookie},
                data=data,
                ssl=self._ssl,
                chunked=None,
            )
        except aiohttp.ClientSSLError as exc:
            raise CannotConnect(
                f"Could not verify SSL certificate of device {self.host}: {exc}"
            ) from exc
        except aiohttp.ClientError as exc:
            raise CannotConnect(
                f"Connection to device {self.host} failed: {exc}"
            ) from exc

        if resp.status != 200:
            raise InvalidResponse(
                f"Received bad HTTP status code from device {self.host}: {resp.status}"
            )

        # NOTE: Un-authorized request will redirect to /login.cgi
        if str(resp.url.path) == "/login.cgi":
            self._authenticated = False
        else:
            self._authenticated = True

        return resp

    async def login(self) -> None:
        """Login to this device."""
        if not self._authenticated:
            await self.request(
                "POST",
                "/login.cgi",
                data={"username": self._username, "password": self._password},
            )

            if not self._authenticated:
                raise InvalidAuth(
                    f"Login to device {self.host} failed due to wrong credentials"
                )

    async def logout(self) -> None:
        """Logout from this device."""
        if self._authenticated:
            await self.request("POST", "/logout.cgi")

    async def update(self) -> None:
        """Update sensor data."""
        if not self._data or (time.time() - self._time) > self._cache_time:
            await self.login()
            resp_status = await self.request("GET", "/status.cgi")
            resp_sensors = await self.request("GET", "/mfi/sensors.cgi")

            try:
                data = await resp_status.json()
                data.update(await resp_sensors.json())
            except aiohttp.ContentTypeError as exc:
                raise InvalidData(
                    f"Received invalid data from device {self.host}: {exc}"
                ) from exc

            status = data.get("status", None)
            if status != "success":
                raise InvalidData(
                    f"Received invalid sensor update status from device {self.host}: {status}"
                )

            self._time = time.time()
            self._data = data

    @property
    def updated(self) -> bool:
        """Return if the device has already been updated."""
        return bool(self._data)

    @property
    def data(self) -> dict:
        """Return device data."""
        if not self._data:
            raise InvalidData(f"Device {self.host} must be updated first")
        return self._data

    @data.setter
    def data(self, data: dict) -> None:
        """Set device data."""
        self._data = data

    @property
    def host_data(self) -> dict:
        """Return the device host data."""
        return self.data.get("host", {})

    @property
    def fwversion(self) -> str:
        """Return the device host firmware version."""
        return self.host_data.get("fwversion", "")

    @property
    def hostname(self) -> str:
        """Return the device host name."""
        return self.host_data.get("hostname", self._host)

    @property
    def lan_data(self) -> dict:
        """Return the device LAN data."""
        return self.data.get("lan", {})

    @property
    def wlan_data(self) -> dict:
        """Return the device WLAN data."""
        return self.data.get("wlan", {})

    @property
    def ip(self) -> str:
        """Return the device IP address from LAN if connected, else from WLAN."""
        lan_connected = self.lan_data.get("status", "") != "Unplugged"
        if lan_connected:
            ip = self.lan_data.get("ip", "")
        else:
            ip = self.wlan_data.get("ip", "")
        return ip

    @property
    def hwaddr(self) -> str:
        """Return the device hardware address from LAN if connected, else from WLAN."""
        lan_connected = self.lan_data.get("status", "") != "Unplugged"
        if lan_connected:
            hwaddr = self.lan_data.get("hwaddr", "")
        else:
            hwaddr = self.wlan_data.get("hwaddr", "")
        return hwaddr

    @property
    def unique_id(self) -> str:
        """Return a unique device id from combined LAN/WLAN hardware addresses."""
        lan_hwaddr = self.lan_data.get("hwaddr", "")
        wlan_hwaddr = self.wlan_data.get("hwaddr", "")
        if lan_hwaddr and wlan_hwaddr:
            return f"{lan_hwaddr}-{wlan_hwaddr}"
        return ""

    @property
    def port_data(self) -> list[dict]:
        """Return the device port data."""
        return self.data.get("sensors", [])

    @property
    def ports(self) -> int:
        """Return the number of available device ports."""
        return len(self.port_data)

    @property
    def model(self) -> str:
        """Return the model name of this device as string."""
        ports = self.ports
        prefix = "mPower"
        suffix = " (EU)" if self._eu_model else ""
        if ports == 1:
            return f"{prefix} mini" + suffix
        if ports == 3:
            return prefix + suffix
        if ports in [6, 8]:
            return f"{prefix} PRO" + suffix
        return "Unknown"

    @property
    def description(self) -> str:
        """Return the device description as string."""
        ports = self.ports
        if ports == 1:
            return "mFi Power Adapter with Wi-Fi"
        if ports == 3:
            return "3-Port mFi Power Strip with Wi-Fi"
        if ports == 6:
            return "6-Port mFi Power Strip with Ethernet and Wi-Fi"
        if ports == 8:
            return "8-Port mFi Power Strip with Ethernet and Wi-Fi"
        return ""

    async def create_sensor(self, port: int) -> MPowerSensor:
        """Create a single sensor."""
        if not self.updated:
            await self.update()
        return MPowerSensor(self, port)

    async def create_sensors(self) -> list[MPowerSensor]:
        """Create all sensors as list."""
        if not self.updated:
            await self.update()
        return [MPowerSensor(self, i + 1) for i in range(self.ports)]

    async def create_switch(self, port: int) -> MPowerSwitch:
        """Create a single switch."""
        if not self.updated:
            await self.update()
        return MPowerSwitch(self, port)

    async def create_switches(self) -> list[MPowerSwitch]:
        """Create all switches as list."""
        if not self.updated:
            await self.update()
        return [MPowerSwitch(self, i + 1) for i in range(self.ports)]
