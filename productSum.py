# “Given two integer numbers return their product only if the product is greater than 1000, 
# else return their sum.
def twoNums(num1,num2):
    product = num1*num2    
    formattedNum1 = format(num1,",")
    formattedNum2 = format(num2,",")
    formattedproduct = format(product,",")
    formattedSum = format(sum)
    if product>1000:
        return "Product of {} and {} is {}".format(formattedNum1,formattedNum2,formattedproduct)
    else:
        return "sum of {} and {} is {}".format(formattedNum1,formattedNum2,formattedSum)

num1 = int(input("First number: "))
num2 = int(input("Second number: "))
print(twoNums(num1,num2))