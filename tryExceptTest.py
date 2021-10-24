try:
    inp = int(input("Number: "))
    if inp == 1:
        print("One")
    elif inp == 1:
        print("two")
    else:
        print("Incorrect choice")
except ValueError:
    print("You didn't enter a number")
