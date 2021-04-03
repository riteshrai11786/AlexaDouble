import pywhatkit

from datetime import datetime

now = datetime.now()

current_time = now.strftime("%H:%M:%S")
#print("Current Time =", current_time)
#print(now.hour)
#print(now.minute + 1)
#pywhatkit.sendwhatmsg('+917702677997', 'How are you?', now.hour, now.minute + 2)
my_string="send whatsapp message to 789 3109 483 that You are cool! "
phone_number = my_string.split("to ",1)[1]
phone_number = "+91" + phone_number.split("that ",1)[0]
phone_number = phone_number.replace(" ", "")
my_msg = my_string.split("that ",1)[1]

print(my_string)
print(phone_number)
print(my_msg)