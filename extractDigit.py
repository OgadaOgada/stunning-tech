#If the given int is 7536, the output shall be “6 3 5 7“, with a space separating the digits.

# def extract(number):
#     length = len(number)
#     reverseIndex = -1
#     newText = ""
#     while length != 0:
#         newText = newText + " "+str(number[reverseIndex])
#         reverseIndex -= 1
#         length -= 1
#     print(newText)
#     return

# ALTERNATIVE
def extract(number):
     newtext = str(number)[::-1]
     newNumber = ""
     for i in newtext:
         newNumber = newNumber+" "+i
     print(newNumber)


extract(input("Number: "))
