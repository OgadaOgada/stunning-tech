ascii_dict = {'A': 65, 'B': 66, 'C': 67, 'D': 68}
# Reverse mapping
new_dict = {value: key for key, value in ascii_dict.items()}
print(new_dict)
list_my = range(10)
print(list(list_my))
mns = [x for x in list_my if x % 2]
print(mns)