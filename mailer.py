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