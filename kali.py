import pywhatkit as kit
import time

# Replace 'contact_number' with the recipient's phone number (including the country code, e.g., +1 for the USA)
contact_number = "+923337989271"

# Replace 'your_message' with the message you want to send
your_message = "Hello, this is an automated message from Kali Linux."

# Number of messages to send
num_messages = 50

# Delay (in seconds) between sending each message
delay = 10  # You can adjust this delay as needed

# Get the current time (hours and minutes)
current_time = time.localtime()
current_hour = current_time.tm_hour
current_minute = current_time.tm_min

# Send the messages
for i in range(num_messages):
    # Calculate the time for each message with a delay
    message_hour = current_hour
    message_minute = current_minute + (i * delay // 60)  # Increment minutes based on delay

    # Adjust hours and minutes if they exceed 60
    while message_minute >= 60:
        message_minute -= 60
        message_hour += 1

    # Send the message
    kit.sendwhatmsg(contact_number, your_message, message_hour, message_minute)
    
    # Pause for the specified delay
    time.sleep(delay)
