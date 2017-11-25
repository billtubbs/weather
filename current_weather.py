#!/usr/bin/env python
import requests
import sys

api_key = "d2ec26ecb98b5ade6acb6b98e55e613b"
url_format_string = 'http://api.openweathermap.org/data/2.5/weather?id={}&APPID={}'


def get_current_weather(city_id=6173331):

    url = url_format_string.format(city_id, api_key)

    try:
        r = requests.get(url, auth=('user', 'pass'))
    except requests.exceptions.ConnectionError:
        return "CONNECT ERROR", None

    if r.status_code != 200:
        return "ERROR {}".format(r.status_code), None
    else:
        return None, r.json()


if __name__ == "__main__":
    print(get_current_weather(*sys.argv[1:]))
