#Print characters from a string that are present at an even index number
import re


def userText(text):
    length = len(text)
    counter = 2
    while counter < length:
        print(text[counter])
        counter += 2
    return

textInput = input("Your text: ")
userText(textInput)