import aiohttp
import asyncio


class Urls:
    confirmed = "http://api.covid19api.com/dayone/country/{country}/status/confirmed"
    recovered = "http://api.covid19api.com/dayone/country/{country}/status/recovered"
    deaths = "http://api.covid19api.com/dayone/country/{country}/status/deaths"


class HttpClient:
    def __init__(self, countries):
        self.countries = countries
        self.results = {}

    @staticmethod
    def _prepare_url(url, country):
        return url.replace('{country}', country)

    async def _get_data_by_country(self, country):
        confirmed = self._prepare_url(Urls.confirmed, country)
        recovered = self._prepare_url(Urls.recovered, country)
        deaths = self._prepare_url(Urls.deaths, country)

        self.results[country] = {}

        async with aiohttp.ClientSession() as session:
            async with session.get(confirmed) as response:
                self.results[country]['confirmed'] = await response.read()

        async with aiohttp.ClientSession() as session:
            async with session.get(recovered) as response:
                self.results[country]['recovered'] = await response.read()

        async with aiohttp.ClientSession() as session:
            async with session.get(deaths) as response:
                self.results[country]['deaths'] = await response.read()

        return self.results

    def get(self):
        coroutines = [self._get_data_by_country(country) for country in self.countries]

        loop = asyncio.get_event_loop()
        loop.run_until_complete(asyncio.gather(*coroutines))

        return self.results
