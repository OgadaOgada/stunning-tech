# create a range of numbers, ast the user for input

begin = ""
end = ""
# creating a function to prompt for user input
def inputpromptInt(text):
    return int(input(text+": "))

# a function, The actual user input of two numbers, start and end
def userInput():
    global begin, end
    begin = inputpromptInt("Range start number")
    end = inputpromptInt("Range end number")

# a function, creating a list of numbers from the user entered values 
# range here gives numbers range from begining to end and list gives as a list
def userRange():
    userInput()
    userList = list(range(begin,end))
    return userList

# a fuction to create lower numbers to divide by the user list
def systemRange(end):
    systemList = list(range(begin,end))
    return systemList


def checkingPrime():
    for i in userRange():
        numFactors = [] # a list to contain factor of a number
        primerChecker = False
        for j in systemRange(i):
            if i % j == 0:
                numFactors.append(j) #appending factors to a list
                primerChecker = True 
        if primerChecker == False:
            print(str(i)+" is a prime number")
        else:
            print("{} is divisible by {}".format(i,list(set(numFactors))))
    return   

checkingPrime()
