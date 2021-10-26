#! python3
myString="This is a string."
print(myString)
print(type(myString))
print(myString+" is of data type "+str(type(myString)))

firstString = "water"
secondString = "fall"
thirdString = firstString+secondString
print(thirdString)

name = "Collince"
age = 50
color = "Blue"
animal = "Cat"
print("{0}, your age is {2}, you like a {3} which is {1}!".format(name,age,color,animal))
print("{0}, your age is {3}, you like a {2} which is {2}!".format(name,age,color,animal))
print("{0}, your age is {0}, you like a {0} whos is {0}!".format(name,age,color,animal))
print("%s, your age is %s, you feel you like a %s %s"%(name,age,color,animal))