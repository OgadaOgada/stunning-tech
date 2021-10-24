with open(".\input.txt", "w") as file:
    try:
       print("no exception")
    except:
        print("exception occured")
total = 0
for i in range(1,201):
    total += i
print(total)
print("My friend! "*4)
