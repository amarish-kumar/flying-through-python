import requests

def get_weather_forecast():
	url = 'http://api.openweathermap.org/data/2.5/weather?q=tijuana&appid=44db6a862fba0b067b1930da0d769e98'
	weather_requests = requests.get(url)
	weather_json = weather_requests.json()
	
	description = weather_json['weather'][0]['description']
	temp_min = weather_json['main']['temp_min']
	temp_max = weather_json['main']['temp_max']
	
	forecast = 'The circus forecast for today is ' + description + ' with a high of '
	forecast += str(temp_max) + ' and a low of ' + str(temp_min)
	
	return forecast