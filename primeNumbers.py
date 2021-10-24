# num = int(input("Enter the number: "))

# if num > 1:
#     # check for factors
#     for i in range(2, num):
#         if (num % i) == 0:
#             print(num, "is not a prime number")
#             print(i, "times", num//i, "is", num)
#             break
#         else:
#             print(num, "is a prime number")
#             # if input number is less than
#             # or equal to 1, it is not prime
# else:
#     print(num, "is not a prime number")

#  natural numbers greater than 1 that cannot be formed by multiplying two smaller natural numbers
# ONLY DISIBILE BY ITSELF AND 1

myRange = range(2,251)
for i in myRange:
    divisibilityCheck = False    
    myDenominatorList = range(2,i) #create a list of numbers lower than the number to be checked
    for j in myDenominatorList:
        if i % j == 0: #checks whether the number is divisble by any lower number greater than one
            # print(str(i)+" is divisible by "+str(j))
            divisibilityCheck  = True #if any number divides the number being checked then, boolean is assigned True
            # print()
    if divisibilityCheck == False:
        print(i)


# def myPrimeNumbers(startNumber,endNumber):
#     myRange = range(startNumber,endNumber)
#     sumPrimeNos = 0
#     for i in myRange:
#         divisibilityCheck = False    
#         myDenominatorList = range(startNumber,i) #create a list of numbers lower than the number to be checked
#         for j in myDenominatorList:
#             if i % j == 0: #checks whether the number is divisble by any lower number greater than one
#                 print(str(i)+" is divisible by "+str(j))
#                 divisibilityCheck  = True #if any number divides the number being checked then, boolean is assigned True
#                 # print()
#         if divisibilityCheck == False:
#             sumPrimeNos += i
#             print(i)
#             print()
#     return format(sumPrimeNos,",")

# rangeStart = int(input("Enter the starting number: "))
# rangeEnd = int(input("Enter the end number: "))

# print("Prime numbers between 0 and 251")
# myPrimeNumbers(rangeStart,rangeEnd)
  