""" Simple Python class to interact with the VG electricity API
"""

import logging
import aiohttp

BASE_URL = "https://redutv-api.vg.no/power-data/"

logger = logging.getLogger('vg-electricity')


class VGElectricity:
    """VG API connection class"""

    def __init__(self):

        self.session = aiohttp.ClientSession()

    async def today(self):
        """Get Today's electricity stats"""
        return await self._get("v2/nordpool/historic/day")

    async def future(self):
        """Get estimated future electricity prices"""
        return await self._get("v1/nasdaq/future-prices")

    async def _get(self, uri):
        """Generic GET request helper function"""
        url = f'{BASE_URL}{uri}'
        async with self.session.get(url) as resp:
            return await resp.json()

    async def close_session(self):
        """Close the connection session"""
        await self.session.close()

    async def sensor_data(self):
        """Get flat json structure for Home Assistant Sensor parsing"""
        data = {}
        data['state'] = "unavailable"

        today = await self.today()

        if today:
            data['state'] = "available"
            current_average = {}
            current_average['oslo'] = today['soFarThisMonth']['oslo']
            current_average['bergen'] = today['soFarThisMonth']['bergen']
            current_average['kristiansand'] = today['soFarThisMonth']['kristiansand']
            current_average['tromso'] = today['soFarThisMonth']['tromso']
            current_average['trondheim'] = today['soFarThisMonth']['trondheim']
            data["current_average_price"] = current_average

        future = await self.future()

        if future:
            estimated_future = {}
            estimated_future['oslo'] = future['regions']['oslo']['periodTypes']['m'][0]['priceNOK']
            estimated_future['bergen'] = future['regions']['bergen']['periodTypes']['m'][0]['priceNOK']
            estimated_future['kristiansand'] = future['regions']['kristiansand']['periodTypes']['m'][0]['priceNOK']
            estimated_future['tromso'] = future['regions']['tromso']['periodTypes']['m'][0]['priceNOK']
            estimated_future['trondheim'] = future['regions']['trondheim']['periodTypes']['m'][0]['priceNOK']
            data["estimated_future_average_price"] = estimated_future
        
        return data
