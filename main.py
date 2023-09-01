import pywhatkit as kit
import time

# Replace 'contact_name' with the name of the contact you want to send the message to
contact_name = "Friend's Name"

# Replace 'your_message' with the message you want to send
your_message = "Hello, this is an automated message from Termux."

# Number of times to send the message
num_messages = 10

# Delay (in seconds) between sending each message
delay = 10  # You can adjust this delay as needed

# Send the message multiple times
for i in range(num_messages):
    kit.sendwhatmsg_instantly(contact_name, your_message)
    time.sleep(delay)
