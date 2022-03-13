import pywhatkit, pyperclip

# snum = input("Phone number: ")
snum = pyperclip.paste()
msg = input("Your message: ")
hour = int(input("Hour: "))
mins = int(input("Minute: "))
try:
   
# pywhatkit.sendwhatmsg("phone number","message",hour(in 24         ), minutes)
    # pywhatkit.sendwhatmsg("+254717109419","Hello, from vscode",12, 19)
    pywhatkit.sendwhatmsg("+254"+snum,msg,hour,mins)
    # pywhatkit.playonyt("How to use pywhatkit") #play youtube video
    print("Successfully Sent!")
 
except Exception as error:
   
  print("An Unexpected Error!"+ error)

  #TO BE COMPLETED LATER