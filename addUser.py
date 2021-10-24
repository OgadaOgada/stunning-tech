
import getpass
# def new_user():
#     confirm = "N"
#     while confirm != "Y":
#         username = str(input("Enter username: "))
#         print("Use the username '"+username+"' ?(Y/N)")
#         confirm = str(input("")).upper()
#         print(confirm)
# # os.system(“sudo adduser “ + username)
# new_user()

# string = "    Collince   Ogada   Otieno    "
# string1 = "     My   name   is "
# #strip() removes the leading spaces at the begining and the end
# print(string1.strip()+string.strip()+"-")
# print(string1.lstrip()+string.lstrip()+"-")
# print(string1.rstrip()+string.rstrip()+"-")
# print()
# snew = (string1+string)+"-"

# print(snew)
# print(snew.strip())
# print(" ".join(snew.split()))
# print(snew.replace(" ",""))

# password = getpass.getpass()
# print(password)

mypass = getpass.getpass("PASSWORD : ")
print(mypass)
mypa = getpass.getuser() #gets logged in user
print(mypa)