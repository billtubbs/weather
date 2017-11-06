#!/usr/bin/env python
import requests
import sys

"""
Python module to fetch current weather informaiton from OpenWeatherMap's
API.

Includes:

get_current_weather(city_id=6173331) -> status_code, json

Returns a status code and a json text string containing information
on the current weather conditions at the specified city id location.

api_key - set this to your OpenWeatherMap API key.

API Reference:
http://openweathermap.org/current
"""


api_key = "{Insert your API key here}"
url_format_string = 'http://api.openweathermap.org/data/2.5/weather?id={}&APPID={}'


def get_current_weather(city_id=6173331):

    url = url_format_string.format(city_id, api_key)

    r = requests.get(url, auth=('user', 'pass'))

    return r.status_code, r.json()


if __name__ == "__main__":
    print(get_current_weather(*sys.argv[1:]))
