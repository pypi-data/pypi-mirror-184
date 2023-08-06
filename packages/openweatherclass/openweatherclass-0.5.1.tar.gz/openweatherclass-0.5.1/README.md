# A Python implementation of the Open Weather API 

To use ➡️

* install from [PyPi](https://pypi.org/project/openweatherclass/).

[OpenWeather Homepage](https://openweathermap.org/)

```shell
pip install openweatherclass
```

* Get an [API](https://openweathermap.org/api) Key

* Initiate the class

```python
import openweatherclass as owc

weather = owc.OpenWeatherClass(api_key=API_KEY, zipcode='02188', units='imperial')
print(weather.geo_data['name'])
print(weather.weather_data['current']['temp'])
```
