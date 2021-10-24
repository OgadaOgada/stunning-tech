from os import error

with open(".\myTrial.txt","w") as file:
    try:
        file.write("This is a fresh start. I have the following to do:\n1. UX\n2. Python\n3. Labs")
        file.close()
    except error as er:
        print(er)
    else:
        print("File written successfully")

with open(".\myTrial.txt", "r") as file:
    try:
        content = file.read()
        print("\nStart of new content")
        print(content)
        print("\n")
    except error as er:
        print(er)

with open(".\myTrial.txt","a") as file:
    try:
        file.write("\nI'm not overwriting anything, I'm just appending some new lines.\nI surely have so much to append!")
        file.close()

    except error as er:
        print(er)

with open(".\myTrial.txt", "r") as file:
    try:
        content = file.read()
        print("\nAfter appending some content")
        print(content)
        print("\n")
    except error as er:
        print(er)