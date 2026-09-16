from unittest.mock import Mock
weather_api = Mock()
weather_api.get_temperature.return_value = "28°C"
print(weather_api.get_temperature())