import pywhatkit as kit

# Replace 'contact_name' with the name of the contact you want to send the message to
contact_name = "Zahir"

# Replace 'your_message' with the message you want to send
your_message = "Hello, this is an automated message from Termux."

# Send the message
kit.sendwhatmsg_instantly(contact_name, your_message)
