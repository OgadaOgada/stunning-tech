# mylaptop = {'speed':'3.2GHZ','color':'gray','ram':'16GB'}
# print(str(mylaptop.keys()))
# mylaptop['color']='black'
# print('My laptop color is '+mylaptop['color'] +" and RAM is "+mylaptop['ram'])

# topicsLearnt = {1:'AWS','two':'Linux',3:'Networking'} #unordered, even if you change the order, it's still the same
# print(topicsLearnt[1])  #returns the value at key 1
# print('two' in topicsLearnt.keys()) #checks whether key two is in the dictionary

# #display the content of the dictionary i.e key, values, and items
# print('Here are the keys '+str(topicsLearnt.keys()))
# print('Here are the values '+str(topicsLearnt.values()))
# print('Here are the items '+str(topicsLearnt.items()))
# print()
# #converting the dictionary items to list then displaying
# print('Here are the keys '+str(list(topicsLearnt.keys())))
# print('Here are the values '+str(list(topicsLearnt.values())))
# print('Here are the items '+str(list(topicsLearnt.items())))
# print()
# print('Here are the keys ')
# for k in topicsLearnt.keys(): # looping iteratively in the dictionary for keys
#     print(k)
# print()

# print('Here are the values ')
# for v in topicsLearnt.values():# looping iteratively in the dictionary for values
#     print(v)
# print()

# print('Here are the items ')
# for i in topicsLearnt.items():# looping iteratively in the dictionary for items
#     print(i)
# print()
# print('Better items ')
# for ik,iv in topicsLearnt.items():# looping iteratively in the dictionary for items
#     print(ik,iv)
# print()

# # FROM AWS labs -- lists, tuples, dictionary
# myFruitList = ["apple", "banana", "cherry"]
# print(myFruitList)
# print(myFruitList[0])
# print(myFruitList[1])
# print(myFruitList[2])
# print(type(myFruitList))

# myFruitList[2] = "Oranges"
# print(myFruitList)

# myFinalAnswerTuple = ("apple", "banana", "pineapple")
# print(myFinalAnswerTuple)
# print(myFinalAnswerTuple[0])
# print(myFinalAnswerTuple[1])
# print(myFinalAnswerTuple[2])
# print(type(myFinalAnswerTuple))

# myFavoriteDictionary = {
#     "Akua" : "apple",
#      "Saanvi" : "banana",
#      "Paulo" : "pineapple"
# }
# print(myFavoriteDictionary)
# print(myFavoriteDictionary["Akua"])
# print(myFavoriteDictionary["Saanvi"])
# print(myFavoriteDictionary["Paulo"])
# print(type(myFavoriteDictionary))

for i in range(4):
    print(i)
# the same as 
for i in [0,1,2,3]:
    print(i)
# list the of a range
print(list(range(4)))
print(list(range(0,100,2)))
ranges = [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 
            36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64, 66, 68,
             70, 72, 74, 76, 78, 80, 82, 84, 86, 88, 90, 92, 94, 96, 98]

# for i in ranges:
#     # print(i)
#     print("Index "+str(i)+" is "+str(ranges[i]))

supplies = ["pens","books","envelopes","erasers"]

mylaptop = ["Core i3","14-inch","16GB","1TB","Windows 10 pro"]
cpu,screenSize,RAMSize,HDDisk,OSVersion = mylaptop
print(cpu)
print(RAMSize)
print(HDDisk)
print(OSVersion)
for i in range(len(supplies)):
    print("Index "+str(i)+" is "+str(supplies[i]))

# swapping two variables without a third one
a = "first"
b = "second"
print(a+" "+b)
a,b = b,a
print(a+" "+b)

mylaptop.append("Something else")
mylaptop.insert(2,"somehting else") #insert new itme at index 2
mylaptop.remove("what to remove")
mylaptop.pop() #last item will be removed and returned for display
mylaptop.pop(i) #the item at index i will be removed and returned for display

del mylaptop[0] #removes the item at index 0
mylaptop.sort() #alphabetically, without any keyword all caps comes first 
print(mylaptop)
# sort in true alphabeticall order with keyword key
mylaptop.sort(key=str.lower)
# You can't sort a list with different data types
mylaptop.sort(reverse=True) #alphabetically
print(mylaptop)

# slicing a string
name = "Collince"
print(name[1:3]) #likke a range that starts from 1 and ends at 2
print(name(-2)) #prints the second char from the last char
print("llin" in name) #returns true or false
name[0] = "K" #will throw an error coz string is immutable


#TO FLATTEN A LIST
#FAST
import itertools

List_2D = [[1,2,3],[4,5,6],[7,8,9]] #List to be flattened

List_flat = list(itertools.chain(*List_2D))

print("Original List:",List_2D)
print("Flattened List:",List_flat)

#FASTER 
import functools
import operator

List_2D = [[1,2,3],[4,5,6],[7,8,9]] #List to be flattened

List_flat = functools.reduce(operator.iconcat, List_2D, [])

print("Original List:",List_2D)
print("Flattened List:",List_flat)


#NOT SO FAST
List_2D = [[1,2,3],[4,5,6],[7,8,9]] #List to be flattened
List_flat = []

for i in range(len(List_2D)): #Traversing through the main list
  for j in range (len(List_2D[i])): #Traversing through each sublist
    List_flat.append(List_2D[i][j]) #Appending elements into our flat_list
    
print("Original List:",List_2D)
print("Flattened List:",List_flat)