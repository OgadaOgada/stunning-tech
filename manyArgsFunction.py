def many_args(*myInts):
    print("Total values entered",len(myInts))
    result = 0
    for x in myInts:
        result += x
    return result
# muns = input("enter nums:")
print("Sum of values entered",many_args(7,4,5,9))


# check1  = False
# check2  = False
# def list_xor(n,list1,list2):
#     global check1
#     if n in list1 and n in list2:
#         check1 = True
          
#     return check1

# myl1 = [1,2,3,4,9]
# myl2 = [45,56,78,3]
# num = 3
# list_xor(num,myl1,myl2)

# # if check1 and check2:
# #     print("Number exist in both lists")

# if check1:
#     print("Number exist in list1")

# # elif check2:
# #     print("Number exist in list2")
# else:
#     print("Number does not exist in both list")