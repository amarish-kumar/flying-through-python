import requests
import smtplib

def get_emails():
	emails = {}
	try:
		email_file = open('emails2.txt', 'r')
		for	line in email_file:
			(email, name) = line.split(',')
			emails[email] = name.strip()
	except IOError as err:
		print(err)
	return emails

def get_schedule():
	try:
		schedule_file = open('schedule.txt', 'r')
		schedule = schedule_file.read()
	except IOError as err:
		print(err)

	return schedule

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

def send_emails(emails, schedule, forecast):
	# connect to smtp server
	server = smtplib.SMTP('smtp.gmail.com', '587')
	# start encryption
	server.starttls()
	# login
	password = raw_input("What's your password?")
	from_email = 'flying.through.python@gmail.com'
	server.login(from_email, password)
	# send_emails
	for to_email, name in emails.iteritems():
		message = 'Subject : welcome to the circus\n'
		message += 'Hi ' + name + '!\n\n'
		message += forecast + '\n\n'
		message += schedule + '\n\n'
		message += 'hope to see you there!'
		server.sendmail(from_email, to_email, message)
	# test
	server.quit()
	
def main():
	emails = get_emails()
	#print(emails)
	schedule = get_schedule()
	#print(schedule)
	forecast = get_weather_forecast()
	#print(forecast)
	send_emails(emails, schedule, forecast)

# minuto 18:10
main()