#printing something at the start of code

# print("Hello, welcome user!")

def welcome_message():
    print("Hello, welcome user!")
print()
# print(__name__)
if __name__ == "__main__":
    welcome_message()


arr = [1,8,15,22]
gen = (x for x in arr if arr.count(x) > 0)
# for x in arr:
#     if arr.count(x) > 0:
#         counter = x
# for x in arr:
#     print(x,arr.count(x))
arr = [2,8,22]
print(list(gen))
# print(arr)
# print(counter)
