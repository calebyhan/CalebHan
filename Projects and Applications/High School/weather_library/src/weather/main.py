import requests

class API:
    def __init__(self, api_key):
        self.api_key = api_key
    

    def __check_api_key(self):
        if self.api_key == "":
            raise ValueError("Empty API Key.")


    def current(self, q, aqi="no", lang=-1):
        self.__check_api_key()
        params = {
            "key": self.api_key,
            "q": q,
            "aqi": aqi
        }
        if lang != -1:
            params.update({"lang": lang})
        return requests.get("https://api.weatherapi.com/v1/current.json?", params=params).json()


    def forecast(self, q, days=3, alerts="no", aqi="no", lang=-1):
        self.__check_api_key()
        params = {
            "key": self.api_key,
            "q": q,
            "days": days,
            "alerts": alerts,
            "aqi": aqi
        }
        if lang != -1:
            params.update({"lang": lang})
        return requests.get("https://api.weatherapi.com/v1/forecast.json?", params=params).json()


    def history(self, q, dt=-1, lang=-1):
        self.__check_api_key()
        params = {
            "key": self.api_key,
            "q": q,
        }
        if dt != -1:
            params.update({"dt": dt})
        if lang != -1:
            params.update({"lang": lang})
        return requests.get("https://api.weatherapi.com/v1/history.json?", params=params).json()


    def future(self, q, dt=-1, lang=-1):
        self.__check_api_key()
        params = {
            "key": self.api_key,
            "q": q,
        }
        if dt != -1:
            params.update({"dt": dt})
        if lang != -1:
            params.update({"lang": lang})
        return requests.get("https://api.weatherapi.com/v1/future.json?", params=params).json()


    def search(self, q, lang=-1):
        self.__check_api_key()
        params = {
            "key": self.api_key,
            "q": q,
        }
        if lang != -1:
            params.update({"lang": lang})
        return requests.get("https://api.weatherapi.com/v1/search.json?", params=params).json()


    def ip(self, q, lang=-1):
        self.__check_api_key()
        params = {
            "key": self.api_key,
            "q": q,
        }
        if lang != -1:
            params.update({"lang": lang})
        return requests.get("https://api.weatherapi.com/v1/ip.json?", params=params).json()


    def astro(self, q, dt=-1, lang=-1):
        self.__check_api_key()
        params = {
            "key": self.api_key,
            "q": q,
        }
        if dt != -1:
            params.update({"dt": dt})
        if lang != -1:
            params.update({"lang": lang})
        return requests.get("https://api.weatherapi.com/v1/astronomy.json?", params=params).json()


    def sports(self, q, lang=-1):
        self.__check_api_key()
        params = {
            "key": self.api_key,
            "q": q,
        }
        if lang != -1:
            params.update({"lang": lang})
        return requests.get("https://api.weatherapi.com/v1/sports.json?", params=params).json()


    def timezone(self, q, lang=-1):
        self.__check_api_key()
        params = {
            "key": self.api_key,
            "q": q,
        }
        if lang != -1:
            params.update({"lang": lang})
        return requests.get("https://api.weatherapi.com/v1/timezone.json?", params=params).json()