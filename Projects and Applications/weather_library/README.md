# weather-ch

Python library for weather information. Docker library for WeatherAPI. This project is unaffiliated with the official company.

Data from [WeatherAPI](https://www.weatherapi.com/).


## Installation
----------------------

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install weather-ch.

```bash
pip install weather-ch
```


## Usage
----------------------

```python
import weather

weatherAPI = weather.API("API KEY HERE")

# returns current weather in London
weatherAPI.current("London")

# returns 3 day forecast of London
weatherAPI.forecast("London")
```


## Documentation
----------------------

``weather.API(api_key)``

[API Key](https://www.weatherapi.com/docs/#intro-authentication)

``weather.current(q, aqi="no", lang=-1)``

[Realtime API](https://www.weatherapi.com/docs/#apis-realtime)

``weather.forecast(q, days=3, alerts="no", aqi="no", lang=-1)``

[Forecast API](https://www.weatherapi.com/docs/#apis-forecast)

``weather.history(q, dt=-1, lang=-1)``

[History API](https://www.weatherapi.com/docs/#apis-history)

``weather.future(q, dt=-1, lang=-1)``

[Future API](https://www.weatherapi.com/docs/#apis-future)

``weather.ip(q, lang=-1)``

[IP Lookup API](https://www.weatherapi.com/docs/#apis-ip-lookup)

``weather.astro(q, dt=-1, lang=-1)``

[Astronomy API](https://www.weatherapi.com/docs/#apis-astronomy)

``weather.sports(q, lang=-1)``

[Sports API](https://www.weatherapi.com/docs/#apis-sports)

``weather.timezone(q, lang=-1)``

[Time Zone API](https://www.weatherapi.com/docs/#apis-timezone)

## Contributing
----------------------

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

Please make sure to update tests as appropriate.


## License
----------------------

[MIT](https://choosealicense.com/licenses/mit/)
