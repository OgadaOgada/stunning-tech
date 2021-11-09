#! python3
import re, pyperclip

#create regex for phone numbers

myPhoneRegex = re.compile(r"""
# 801-997-4158, 801-0000,(801) 997-00000, 997-0000,ext 12345, ext. 12345, x12345
#((\d\d\d) | (\(\d\d\d)))?   #area code (optional)
\d\d\d  #area code (optional)
#  (\s | -)   #first separator
-   #first separator
 \d\d\d   #first 3 digits
-   #separator
\d\d\d\d  #last four digits
  #((ext(\.)?\s) | x)
  #(\d{2,5})
""", re.VERBOSE) #verbose mode helps in having comments

#create a regex for email address
emailRegex = re.compile(r"""
#some.+_thing@something.com -->  [a-zA-Z0-9_.+]+@[a-zA-Z0-9_.+]+  one or more char@one or more char
[a-zA-Z0-9_.+]+ #name part
@ #@symbol
[a-zA-Z0-9_.+]+  #domain name part
""",re.VERBOSE)


#get the text off the clipboard
text = pyperclip.paste()

#Extract the email/phone from this text
extractedPhone = myPhoneRegex.findall(text)

#copy the extracted email/phone to the clipboard
extractedEmail = emailRegex.findall(text)

allPhoneNumbers = []
allEmailAddresses = []

with open ("phoneNumbersText.txt","w") as phoneNumberFile:
    for phoneNumber in extractedPhone:
        # allPhoneNumbers.append(phoneNumber)
        phoneNumberFile.write(phoneNumber+"\n")
        # print(phoneNumber)
    print("Phone number file created successfully")

with open ("emailAddresses.txt","w") as emailAdressFile:
    for emailAddress in extractedEmail:
        # allEmailAddresses.append(emailAddress)
        emailAdressFile.write(emailAddress+"\n")
    print("Email addresses file created successfully")
        
# print(allPhoneNumbers)
# print(extractedEmail)