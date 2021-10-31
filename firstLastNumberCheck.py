
# Write a function to return True if the first and last number of a given list is same.
# If numbers are different then return False.
def compare():
    mylist = [10,2923,23923,91,110]
    if mylist[0] == mylist[-1]:
        return True
    else:
        return False
print(compare())