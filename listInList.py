mylist = [[10,20,40,50,30],[["Collince","Fred","Rolex","Shally"],[5.8,6.2,5.0]]]
print("First "+str(mylist [0][0]))
print("Last "+str(mylist[-1][-1][-1]))
print("Sliced list"+str(mylist[-1][0][-3:-1]))

#combine the two last list to index one
print(str(mylist))
mylist[1] = ["Collince","Fred","Rolex","Shally",5.8,6.2,5.0]
print(str(mylist))
print()

#adding items to the first index of initial list
mylist[0][5:]= ["Collince","Fred","Rolex","Shally",5.8,6.2,5.0]
print("Combined")
print(str(mylist))

#deleting list items
print("\n before deleting")
print(str(mylist[0:]))
del mylist[1]
print("\nafter deleting")
print(str(mylist[0:]))
print()

#starts at index 0 and prints up to 3
print("Start at 0 up 4 by [0:4]")
print(str(mylist[0][:4]))
#starts at index 1 and prints everythin up to the last one
print("start from one upto last by [1:]")
print(str(mylist[0][1:]))

print("Getting length")
print(str(len(mylist[0])))

print()
myString = "Collince O. Ogada"
mylist = list(myString)
print(mylist)
print("C" in mylist) #evaluates to true because c is in my list
print("C" not in mylist) #evaluates to false because c is in my list
