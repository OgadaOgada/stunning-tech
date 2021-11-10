#! python3
import re, pyperclip

# JUST TO SHOW THE VERBOSE FORMAT BUT NOT USING IT HERE
my_compile = re.compile(r"""
\d\d\d  #area code
-
\d\d\d  #first three digits
-
\d\d\d  #second three digits
-
\d\d\d  #last three digits
""",re.VERBOSE | re.IGNORECASE | re.DOTALL) #using the bitwise operator/pipe


#READING CONTENT OF A TEXT FILE AND FINDING PHONE NUMBERS IN IT

#phone numbers regex
phoneRegex = re.compile(r"\d\d\d-\d\d\d-\d\d\d\d")

#request the user to type the file then read text file into content variable
theFile = input("File name: ")
with open ("Q:\Learning\Python\stunning-tech\\"+theFile+".txt","r") as file:
    content = file.read()
    # print(content)

#USING PYPERCLIP TO PASTE COPIED TEXT
# copiedText = pyperclip.paste()

matchedPhoneNumbers = phoneRegex.findall(content)
# print(matchedPhoneNumbers)
# matchedPhoneNumbers = phoneRegex.findall(copiedText)

#WRITING THE EXTRACTED PHONE NUMBERS INTO A TEXT FILE BEARING THE FILE NAME
with open (theFile+"_phone_numbers.txt", "w") as file:
    counter  = 1
    for i in matchedPhoneNumbers:
        # JUST FOR ALIGNING THE PHONE NUMBERS
        if len(str(counter)) == 1:
            i = str(counter)+":    "+i

        elif len(str(counter)) == 2:
            i = str(counter)+":   "+i

        elif len(str(counter)) == 3:
            i = str(counter)+":  "+i

        elif len(str(counter)) == 4:
            i = str(counter)+": "+i
        file.write(i+"\n") 
        counter += 1