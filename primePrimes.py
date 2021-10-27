# create a range of numbers, ast the user for input

begin = ""
end = ""
def inputpromptInt(text):
    return int(input(text+": "))

def userInput():
    global begin, end
    begin = inputpromptInt("Range start number")
    end = inputpromptInt("Range end number")

def userRange():
    userInput()
    userList = list(range(begin,end))
    return userList

def systemRange(end):
    systemList = list(range(begin,end))
    return systemList
    
def checkingPrime():
    for i in userRange():
        numFactors = []
        primerChecker = False
        for j in systemRange(i):
            if i % j == 0:
                numFactors.append(j)
                primerChecker = True 
        if primerChecker == False:
            print(str(i)+" is a prime number")
        else:
            print("{} is divisible by {}".format(i,list(set(numFactors))))
    return   

checkingPrime()
