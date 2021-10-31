# Given a two list of numbers, write a program to create a new list such that the new list 
# should contain odd numbers from the first list and even numbers from the second list.
def myFunct(list1, list2):
    list3 = []
    for i in list1:
        if i % 2 != 0:
            list3.append(i)
    for i in list2:
        if i % 2 == 0:
            list3.append(i)
    print()
    print("List 1: "+str(list1))
    print("List 2: "+str(list2)+"\n")
    print("List 3: "+str(list3))
    return

start1 = int(input("list one start num: "))
end1 = int(input("list one  end num: "))
start = int(input("list two start num: "))
end = int(input("list two  end num: "))
list1 = list(range(start1,end1))
list2 = list(range(start,end))
myFunct(list1,list2)

