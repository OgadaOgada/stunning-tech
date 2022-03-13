# from email import message
import smtplib, ssl

# port = 465 #for ssl
# smtp_server = "smtp.gmail.com"
# sender_email = "emailpython10@gmail.com"
# receiver_email = "collinceogada@gmail.com"
# password = "Milicent2013"
# mymessage = """\
# Subject: Hi there

# This message is sent from Python."""
# context  = ssl.create_default_context()
# with smtplib.SMTP_SSL(smtp_server,port,context=context) as server:
#     try:
#         server.login(sender_email,password)
        
#         # PENDING will check how to create a subject
#         res = server.sendmail(sender_email,receiver_email,mymessage)
#         print("Email sent!")

#     except Exception as error:
#         print(error)




port = 465  # For SSL or 465
smtp_server = "smtp.gmail.com"
sender_email = "emailpython10@gmail.com"  # Enter your address
receiver_email = "collinceogada@gmail.com"  # Enter receiver address
password = 'Milicent2013' 
message = """\
Subject: Hi there

This message is sent from Python."""

try:
    server = smtplib.SMTP_SSL('smtp.gmail.com', port)
    server.ehlo()
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message)
except Exception as e:
    print(e)

# or

context = ssl.create_default_context()

with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message)

    #TO BE COMPLETED LATER