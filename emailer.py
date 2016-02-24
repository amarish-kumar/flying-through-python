import weather
import mailer

def get_schedule():
	try:
		schedule_file = open('schedule.txt', 'r')
		schedule = schedule_file.read()
	except IOError as err:
		print(err)

	return schedule
	
def main():
	emails = mailer.get_emails()
	#print(emails)
	schedule = get_schedule()
	#print(schedule)
	forecast = weather.get_weather_forecast()
	#print(forecast)
	mailer.send_emails(emails, schedule, forecast)

# minuto 18:10
main()