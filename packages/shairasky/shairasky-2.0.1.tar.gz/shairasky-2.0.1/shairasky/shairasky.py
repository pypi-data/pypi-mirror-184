import requests

class Weather:
    """Creates a Weather object getting an apikey as input
    and either a city name or lat and lot coordinates

    Package use example:

    # Create a weather object using a city name:
    # The api key bellow is not guaranteed to work.
    # Get you own apikey from https://openweathermap.org
    # And wait a couple of hous for the apikey to be activated

    >>> wather1 = Wather(apikey="26631f0f41b95fb9f5ac0df9a8f43c92", city="Prague")

    # Get complete wather data for the next 12 hours:
    >>> weather1.next_12h()

    # Simplified data for the next 12 hours
    >>> weather1.next_12h_simplified()

    Sample url to get sky condition icons
    http://openweathermap.org/img/wn/10d@2x.png
    """
    def __init__(self, apikey, city=None, lat=None, lon=None):
        if city:
            url = f"https://api.openweathermap.org/data/2.5/forecast?q={city}&APPID={apikey}&units=metric"
            r = requests.get(url)
            self.data = r.json()
        elif lat and lon:
            url = f"https://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&APPID={apikey}&units=metric"
            r = requests.get(url)
            self.data = r.json()
        else:
            raise TypeError("Provide either a city or lat and lon arguments")
        
        if self.data["cod"] != "200":
            raise ValueError(self.data["message"])


    def next_12h(self):
        """Returns 3-hour data for the next 12 hours as a dict.
        """
        return self.data['list'][:4]

    def next_12h_simplified(self):
        """Returns date, temperature, and sky condition every 3 hours
        for the next 12 hours as a tuple of tuples.   
        """
        simple_data = []
        for dicty in self.data['list'][:4]:
            simple_data.append((dicty['dt_txt'], dicty['main']['temp'], dicty['weather'][0]['description'], dicty['weather'][0]['icon']))
        return simple_data

# weather = Weather(apikey="26631f0f41b95fb9f5ac0df9a8f43c92", city="Prague")
# print(weather.next_12h_simplified())