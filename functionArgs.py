# def myf(**ct):
#     print(ct)
#     print("Dictionary keys "+str([*ct]))
#     print("Dictionary values "+str([*ct.values()]))
#     if 'fruit' in ct:
#         print("My fruit of choice {}".format(ct['fruit']))
#     else:
#         print("I did not find any fruit here")
    
# myf(kk='apple', veggie = 'lettuce',fruit='Banana',drink="Water")

def person(name,*data):
    print(name)
    print(data)

person("Collince",23,"Kahawa","Male","Employed")
print("\n\n")

def person(Name,**data):
    # print(fname)
    # print(age)
    print(Name)
    for i,j in data.items():
        print(str(i)+":",j)

user_age = input("Your age: ")
user_fullname = input("Your name: ")
user_resident = input("Your place of resident: ")
user_gender = input("Your gender: ")
user_employment_status = input("Your employment status: ")
person(Age=user_age, Name = user_fullname, Resident=user_resident, Gender=user_gender, Employment_status=user_employment_status)