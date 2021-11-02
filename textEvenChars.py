#Print characters from a string that are present at an even index number

# def userText(text):
#     length = len(text)
#     counter = 0
#     while counter < length:
#         print(text[counter])
#         counter += 2
#     return

def evenchr(str):
	for i in str[0::2]: # start from 0, go upto the last and skip by 2
		print(i)

textInput = input("Your text: ")
# print("old")
# userText(textInput)
# print("\nnew")
evenchr(textInput)
