
mylist = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
# for i in mylist:
#     if i>50:
#         mylist.pop(i)
#     print(i)

for i in range(len(mylist) - 1, -1, -1):
    if mylist[i] > 50:
        del mylist[i]
print(mylist)