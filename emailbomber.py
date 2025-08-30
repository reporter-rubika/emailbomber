import smtplib
from email.mime.text import MIMEText
import time
from termcolor import colored

title = """
            ..,;:ccc,.
          ......
.....
..........,:ld;
           .;;;:::;,,.x,
      ..`.            0Xxoc:,.  ...
  ....                ,ONkc;,;cokOdc,.
 .                   OMo           :ddo.
                    dMc               :OO;
                    0M.                 .:o.
                    ;Wd
                     ;XO,
                       ,d0Odlc;,..
                           ..,;:cdOOd::,.
                                    .:d;.:;.
                                       'd,  .
                                         ;l   ..
                                          .o
                                            c
                                            .
                                             .
 
"""
print(colored(title, 'white', attrs=['bold', 'underline']))
print(colored("Kasra hacker", 'white', attrs=['bold', 'reverse']), end=' ')
print(colored("Khalegh-robot", 'blue'))

EMAIL_ADDRESS = input("what is your email address?:  ")
EMAIL_PASSWORD = input("Enter your APP PASSWORD please!:  ")
RECIPIENT_EMAIL = input("who is reciver?:  ")
SUBJECT_PREFIX = input("subject:  ")
BODY_MESSAGE = input("body:  ")

try:
    NUM_EMAILS_TO_SEND = int(input("number of emails?:  "))
except ValueError:
    print(colored("number is not corect", 'red'))
    exit()

SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 587

def send_email(subject, body, to_email):
    msg = MIMEText(body, 'plain', 'utf-8')
    msg['Subject'] = subject
    msg['From'] = EMAIL_ADDRESS
    msg['To'] = to_email

    try:
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()
            server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            server.send_message(msg)
        return True
    except Exception as e:
        print(colored(f"Eror in send!: {e}", 'red'))
        return False

print(colored(f"start{NUM_EMAILS_TO_SEND} email", 'green'))

for i in range(1, NUM_EMAILS_TO_SEND + 1):
    print(colored(f"Email {i} send...", 'green'))
    subject = SUBJECT_PREFIX + str(i)

  
    RECIPIENT_EMAIL_i = input(f"Keep enter!): ")
    if RECIPIENT_EMAIL_i.strip() == "":
        to_email_final = RECIPIENT_EMAIL
    else:
        to_email_final = RECIPIENT_EMAIL_i.strip
