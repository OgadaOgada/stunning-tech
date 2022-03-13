import itertools,os
import pyperclip
import re

my_path = r"Q:\Learning\Python\stunning-tech"
os.chdir(my_path) #change the working file path to this

nums_group = [
    [1,2,3,4,5,6,7,8,9,0],
    [1,2,3,4,5,6,7,8,9,0],
    [1,2,3,4,5,6,7,8,9,0],
    [1,2,3,4,5,6,7,8,9,0],

    [1,2,3,4,5,6,7,8,9,0],
    [1,2,3,4,5,6,7,8,9,0],
    [1,2,3,4,5,6,7,8,9,0]
    
]

# Expected result
# [1234 1234 1234 1234]
temp_list = []
my_list = list(itertools.product(*nums_group))
ctr = 0
with open ("Credit_cards.doc","a") as doc:
    pass
    # for i in my_list:
    #     # temp_list.append(i)
    #     doc.write(str(i)+"\n")
    #     ctr += 1
    #     if ctr % 5_000_000 == 0:
    #         print(i)
    #     doc.close
    # copied_nums = pyperclip.copy(str(temp_list))
     

# my_regex = re.compile(r"[(2,4,1,9)]")
# mo = my_regex.findall(copied_nums)
# print(mo)
os.startfile(my_path)