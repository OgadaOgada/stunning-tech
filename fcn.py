# from random import *
# import sys, os, math etc
import random
import sys #sys.exit()
# def myFunct(a,b):
#     return a+b

# print('What is the first number?')
# num1 = input()
# print('What is the second number?')
# num2 = input()
# print(myFunct(int(num1),int(num2)))
# 1 + 2 
# sum = 10
# sum %= 60
# # print(sum)
# mylaptop = {'speed':'3.2GHZ','color':'gray','ram':'16GB'}
# print(str(mylaptop.keys()))
# print("Collince"+5)
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
# print('Beter items ')
# for ik,iv in topicsLearnt.items():# looping iteratively in the dictionary for items
#     print(ik,iv)
# print()

# #in lists and tuples the order of the items matter but in dictionary, it doesn't matter (after all it's a dictionary)

# mylist1 = [1,2,3,4]
# nam = 6
# for igg in mylist1:
#     if igg == nam:
#         print("hey")

# else:
#     print('Register')



# kenai2 = ["Ken","Diana","Felix","George"]
# username = input('Enter your username ')
# isExist = False
# for names in kenai2:
#     if names == username:
#         isExist = True    
#         break
# # else:
# #     isExist = False
# if isExist:
#     print('Login successful')
#     print(str(type(kenai2)))
# else:
#     print('Username does not exist')
#     print(str(type(kenai2)))



# mylist2 = [4,3,2,1]

# mytuple1 = (1,2,3,4)
# mytuple2 = (4,3,2,1)

# mydict1 = {1,2,3,4}
# mydict2 = {3,1,4,2}

# print('Is my list 1 equals list 2?\n'+ str( mylist1 == mylist2))
# print('Is my tuple 1 equals tuple 2?\n'+ str( mytuple1 == mytuple2))
# print('Is my dict 1 equals dict 2?\n'+ str( mydict1 == mydict2)) 

# num = 4
# if num<2 & num>=1:
#     print('Between 2 and 1')
# else:
# #     print('Now now')
# mylist = [1,2,3,4,5,6,7]
# lis2 = ['a','r','t']
# for i in mylist:
#     for c inlis2:
#         print(i)
#         print(c)
# coun = 0
# while coun<10:
#     print('Hey')
#     coun++