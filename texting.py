import smtplib
import sys
from creds import EMAIL, PASSWORD

CARRIERS = {
    "att": "@mms.att.net",
    "tmobile": "@tmomail.net",
    "verizon": "@vtext.com",
    "sprint": "@messaging.sprintpcs.com"
}
 

 
def send_message(phone_number, carrier, subject, message):
    recipient = phone_number + CARRIERS[carrier]
    auth = (EMAIL, PASSWORD)
 
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(auth[0], auth[1])
 
    server.sendmail(auth[0], recipient, 'Subject: {}\n\n{}'.format(subject, message))
    server.quit()
 
 
if __name__ == "__main__":
    if len(sys.argv) < 5:
        print(f"Usage: python3 {sys.argv[0]} <PHONE_NUMBER> <CARRIER> <SUBJECT> <MESSAGE>")
        sys.exit(0)
 
    phone_number = sys.argv[1]
    carrier = sys.argv[2]
    message = sys.argv[4]
    subject = sys.argv[3]
 
    send_message(phone_number, carrier, subject , message)