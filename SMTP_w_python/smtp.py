from string import Template
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
"""
Here are four basic steps for sending emails using Python:

    Set up the SMTP server and log into your account.
    Create the MIMEMultipart message object and load it with appropriate headers for From, To, and Subject fields.
    Add your message body.
    Send the message using the SMTP server object.
    """

#Set your credentials here
MY_ADDRESS = 
PASSWORD = 



# First we get the contact names from the list

def get_contacts(filename):
	names = []
	emails = []
	with open(filename, mode='r', encoding='utf-8') as contacts_file:
		for a_contact in contacts_file:
			#footprint 
			print(a_contact)
			names.append(a_contact.split()[0])
			emails.append(a_contact.split()[1])
	return names, emails


#We them need to reasdf rom the template files and return a template object made from the content
def read_template(filename):
	with open(filename, 'r', encoding='utf-8') as template_file:
		template_file_content = template_file.read()
	return Template(template_file_content)

def main():

	names, emails = get_contacts('mycontaxts.txt') # read contacts
	message_template = read_template('message.txt')

	s = smtplib.SMTP(host='smtp.gmail.com', port=587)
	s.starttls()
	s.login(MY_ADDRESS, PASSWORD)

	#For each contact send email
	
	
	for name, email in zip(names, emails):
		msg = MIMEMultipart()       # create a message

		# add in the actual person name to the message template
		message = message_template.substitute(PERSON_NAME=name.title())

        # Prints out the message body for our sake
		print(message)

        # setup the parameters of the message
		msg['From']=MY_ADDRESS
		msg['To']=email
		msg['Subject']="This is TEST"
        
        # add in the message body
		msg.attach(MIMEText(message, 'plain'))
        
        # send the message via the server set up earlier.
		s.send_message(msg)
		del msg
       
        
    # Terminate the SMTP session and close the connection
	s.quit()
  

if __name__ == '__main__':
	main()