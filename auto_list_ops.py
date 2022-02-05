import math

def prompt(text):
    return input(text)

def prompt_float(text):
    return float(prompt(text))

def prompt_int(text):
    return int(prompt(text))

#operations
def Addittion(x,y):
    return x+y

def Subtraction(x,y):
    return x-y

def Multiplication(x,y):
    return x*y

def Division(x,y):
    return x/y

def Power(x,y):
    return pow(x,y)

def Cube(x,y):
    return x*x*x

def Square_root(x,y):
    # return format(math.isqrt(x), ",") #returns the integer part of the square root
    return math.sqrt(x) #returns the square root including decimal part

def Cube_root(x,y):
    return x**(1./3) #** is for exponenet/or reaised to power...raising to power a third is same as finding cube root

def Quit():
    pass

def decimal_places(answer):    
    dp = input("Decimal places? (enter number): ")
    print()
    print("{} correct to {} decimal place(s) is:\n".format(answer,dp))
    return format(answer, ",.{}f".format(dp))+"\n"

#this is a dictionary to called by a dispatcher
my_dict = { "Addittion":Addittion,"Cube":Cube, "Subtraction":Subtraction, "Multiplication":Multiplication, 
"Division":Division, "Power":Power, "Square_root":Square_root, "Cube_root":Cube_root, "Quit":Quit} 

#convertion so as to use index
my_list = list(my_dict)

one_num_func = ["Square_root","Cube","Cube_root"] #list of single number operations
good_bye = "Good bye boss!\n"

#a dispatcher function, enable calling the function with a string input from user
def call_func(func,x=1,y=1): #initialized x and y for funstions with only one numbe like cube etc
    try:
        return my_dict[func](x,y)
    except:
        return "Invalid function"

#getting user selected operation from the list
def my_input():
        
    try:
        user_input = prompt_int("Operation choice (enter number): ")
        num1 = 1
        num2 = 1
        if user_input <= len(my_list):
            #getting index from user input(user_input-1) then getting the item at that index
            predefined_func = my_list[user_input-1] #getting the text value by index using the selected number minus 1 
            print("User selected {} \n".format(predefined_func))

            if predefined_func == "Quit":
                print(good_bye)
                quit()

            elif predefined_func in one_num_func :
                num1 = prompt_float("Number: ")

            else:
                num1 = prompt_float("First number: ")
                num2 = prompt_float("Second number: ")

            returned_answer = call_func(predefined_func,num1,num2)
            print(decimal_places(returned_answer))
        #user input is not right....
        else:
            print("Invalid choice")
            return another_task()

    except Exception as error:
        print("Error, check the value entered and try again\n")

#loop for new tasks
def another_task():
    user_choice = prompt("Perform another operation? (y/n) ").upper()

    yes_choice = ["Y","YES"]
    no_choice = ["N","NO"]

    if user_choice in yes_choice:
        return my_menu()
    elif user_choice in no_choice:
        print(good_bye)
        quit()
    else:
        print("Please enter yes/y to continue or no/n to quit\n")
        another_task()

#print the items on the list from the dictionary
def my_menu():
    for i in my_list:
        print(my_list.index(i)+1,i)
        
    my_input()
    another_task()

my_menu()


#TO IMPROVE ON THIS LATER

