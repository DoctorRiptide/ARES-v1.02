# Import modules / protocols
import smtplib
import random
import time

# NOTICES
# This is ARES v1.02

"""
Important vars:
HOST, PORT, RECIEVER, server, SUBJECT, BODY, message, ADDRESS, PASS

Email send limit as of now:
575 emails

"""

# Connectivity
HOST = 'smtp.google.com'
PORT = 587
PORT_STR = '587'
disconnect_prevent = 0

# Errors
error = ' {-}'
ServerNotConnected = '{-} Server failed to connect to ' + HOST + PORT_STR + error
SenderRefused = '{-} The sender refused the connection. Now delaying for 15 seconds {-}'

server = smtplib.SMTP('smtp.gmail.com', 587)
server.ehlo()
server.starttls()
server.ehlo()
print('{+} Server set {+}')

# Login
SENDER = 'senderemail@gmail.com'
PASS = 'password123!' 
# OR
# SENDER = input('Email Addr: ')
# PASS = input('Password: ')
server.login(SENDER, PASS)

"""
MAKE SURE THAT LESS SECURE APPS IS ENABLED TO CONNECT
"""

print('{+} Login sucsessful {+}')

# Message set up
SUBJECT = input('Subject : ')
BODY = input('Body : ')
message = 'Subject: {subject} \n\n {body}'
print('{+} Message set {+}')

# Set a send amount
SEND_AMOUNT = 10000
SEND_AMOUNT = int(SEND_AMOUNT)
print('{+} Amount set {+}')

# Define the email loop
def SendEmailLoop():
    # DELAY TO PREVENT HTTP 429
    time.sleep(1)
    file1 = open('names.txt', 'r')
    file1_data = file1.readlines()
    name_list = []
    for item in file1_data:
        item = item.strip('\n')
        item = item.lower()
        name_list.append(item)
    
    # Last names
    file2 = open('lastnames.txt', 'r')
    file2_data = file2.readlines()
    lastname_list = []
    for item in file2_data:
        item = item.lower()
        item = item.strip('\n')
        lastname_list.append(item)

    # Set up the reciever
    first = name_list[random.randint(0,125)]
    last = lastname_list[random.randint(0,125)]
    number_suffix = str(random.randint(0,9))
    email_suffix = '@gmail.com'
    RECIEVER = first + last + number_suffix + email_suffix
    first = 0
    last = 0
    number_suffix = 0
    time.sleep(0.5)
    server.sendmail(SENDER, RECIEVER, message)
    print('Message sent to {} from {}'.format(RECIEVER, SENDER))

# Set email loop
message_loop = 0
while message_loop < SEND_AMOUNT:
    try:
        SendEmailLoop()
    except Exception:
        pass
    # HTTP:/429 Send Limit; Restriction
    if disconnect_prevent > 75:
        disconnect_prevent = 0
        print('{I} Delaying for 30 seconds to prevent a disconnect {I}')
        time.sleep(30)

    disconnect_prevent += 1
    message_loop += 1
