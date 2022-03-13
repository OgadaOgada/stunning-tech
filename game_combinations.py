import itertools
import os

os.chdir(r"Q:\Learning\Python\stunning-tech") #change the working file path to this

# #Screen Clearing Function
def clearConsole():
    my_os = ['nt','dos']
    command = 'clear'
    # if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
    if os.name in my_os:  # If Machine is running on Windows, use cls
        command = 'cls'
    return os.system(command)
clearConsole()


# 1: Home team win         x: Draw         2: Away team win
group_outcome = [
    ["1","x","2"], #game 1
    ["1","x","2"], #game 2
    ["1","x","2"], #game 3
    ["1","x","2"], #game 4
    # ["1","x","2"], #game 5

    # ["1","x","2"], #game 6
    # ["1","x","2"], #game 7
    # ["1","x","2"], #game 8
    # ["1","x","2"], #game 9
    # ["1","x","2"], #game 10
    
    # ["1","x","2"], #game 11
    # ["1","x","2"], #game 12
    # ["1","x","2"], #game 13
    # ["1","x","2"], #game 14
    # ["1","x","2"], #game 15
    
    # ["1","x","2"], #game 16
    # ["1","x","2"]  #game 17
]

my_list = list(itertools.product(*group_outcome))

my_counter = 0
file_name = "17_games_combinations.txt"

# with open (file_name,"a") as file:
#     pass
#     for i in my_list:
#             file.write(str(i)+"\n")
#             # print(i)
#             file.close
#             my_counter += 1
#             if my_counter % 5_000_000 == 0:
#                 print(my_counter)
# print("Completed successffully")
# print("Total combinations",my_counter)
# # os.startfile(file_name)
# # print(file_name+" size: ", os.path.getsize(file_name),"bytes")
# print(file_name+" size: ", int(os.path.getsize(file_name)/(1024*1024*1024)),"GB")
for i in my_list:
        print(i)