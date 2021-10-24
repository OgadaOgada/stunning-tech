from logging import ERROR
from os import error


print(476 <= 5)
#print() function returns none
# spam = print()
# print(spam)

# #printing two separate print() in one line
# #
print("line one", end="")
print("line two")

print("one","two","three","four","five") #will create space between the arguments
print("one","two","three","four","five", sep="--") #adding a word separater

spam = 42 #global variable
def eggs():
    spam = 42 #local variable
    return spam
eggs()
print(eggs())
print("some code here")

#Global and local variables
# local variable can't use global variable unless by the global
def spam():
    global eggs
    eggs += 10
    print(eggs)

eggs = 3
spam()
print(eggs)
print()

def divBy(divby):
    try:
        return 30/divby
    except:
        print(except)

print(divBy(2))
print(divBy(0))
print(divBy(10))
print(divBy(3))