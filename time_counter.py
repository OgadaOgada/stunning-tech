import time
timer = 1
counter = 0
mins = 0
maxmin = int(input("Minutes: "))
print("Counting seconds!")
while mins < maxmin:
    time.sleep(1)
    if timer != 60:
        print(timer)
    if timer % 60 == 0:
        mins += 1
        timer = 0
        if mins == 1:
            print(mins," minute")
        else:
            print(mins," minutes")
        # break
    counter += 1
    timer +=1
print()
print(f'{counter} seconds elapsed')
print(f'{mins} minutes elapsed')

