
import os

# #Screen Clearing Function
def clearConsole():
    my_os = ['nt','dos']
    command = 'clear'
    # if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
    if os.name in my_os:  # If Machine is running on Windows, use cls
        command = 'cls'
    return os.system(command)

clearConsole() #clear the console abefore displaying the output

# class Student:
#     school_fee = 130_000 #a class attribute, stays the same for all the instances, _ is to make the it more readable

#     def __init__(self,name,gender,reg_number,course): #class constructor
#         self.name = name
#         self.gender = gender
#         self.reg_number = reg_number
#         self.course = course

#     def student_details(self):
#         print()
#         print("Student name is "+self.name)

# class Text_book:
#     def __init__(self, title, yop):
#         self.title = title
#         self.yop = yop

#     def book_details(self):
#         print("Book title: {}, was published on {}".format(self.title,self.yop))
        
# #TAKE AWAY PORTION
# # get a list of all the attribute of a single object in class and apply print to them  e.g print sname,sgender,sreg_number,scourse for student1



# name = "Collince Otieno Ogada"
# gender = "Male"
# reg_number = "IN13/20079/11"
# course = "Computer Science"

# Student.school_fee = 102_000   #changing class attribute change classwide value
# student1 = Student(name,gender,reg_number,course) #instantiating the student class, a new istance
# student1.school_fee = "Fully sponsored" #changing the value at instance attribute

# text_book1 = Text_book("Things fall a part",2002)

# # student1.student_details()
# print(student1.school_fee)

# student1.text_book_owned = text_book1
# student1.text_book_owned.book_details()
# print()



# class Jog:
#     def details(self):
#         print("Username: "+self.name)
    
# c = Jog()
# c.name = "Collince O." #if you mispel the name it won't work, that's why __init__ constructor is the best
# c.details()

# class Jog_With_init:
#     def __init__(self,name="",gender=""):
#         self.name = name
#         self.gender = gender

#     def details(self):
#         print("Username: "+self.name)
#         print("Gender: "+self.gender)
    
#     def set_age(self,age):
#         self.age = age

# c2 = Jog_With_init("Calvin Klein", "Male")
# # c2.gender = "Male"
# # c2.name ="Collince O. Ogada" #these are what is replaced by __init__, coz you pass the values to the class when instantiating it
# print()
# c2.details()

class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def get_grades(self):
        return self.grade

    def student_name(self):
        return self.name

class Course:
    def __init__(self, name, max_students):
        self.name = name
        self.max_students = max_students
        self.students = []

    def add_students(self,student):
        if len(self.students) < self.max_students:
            self.students.append(student)
            return True
        return False

    def get_average_grade(self):
        value = 0
        for student in self.students:
            value += student.get_grades()
        return "Total grade: {}, mean grade {}".format(value,value / len(self.students))

s1 = Student("Collince",20,50)
s2 = Student("Ghatia",42,80)
s3 = Student("Jane",13,20)
s4 = Student("William",84,90)

course = Course("Computer Science",3)

if course.add_students(s1):
    print("Successfully added ",s1.student_name())
else:
    print("Failed to add ",s1.student_name())

if course.add_students(s2):
    print("Successfully added ",s2.student_name())
else:
    print("Failed to add ",s2.student_name())

if course.add_students(s3):
    print("Successfully added ",s3.student_name())
else:
    print("Failed to add ",s3.student_name())

if course.add_students(s4):
    print("Successfully added ",s4.student_name())
else:
    print("Failed to add ",s4.student_name())

print(course.students[0].name)
# print(s1.get_grades())
print(course.get_average_grade())

for i in course.students:
    print(i.name,i.get_grades())






#INHERITANCE
print()
print("Inheritance")
class Pet:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    
    def speak(self):
        print("This will be printed only when the child class has no similar function by name")

    def show(self):
        print(f"I am {self.name} and I am {self.age} years old")
        # print("I am {} and I am {} years old".format(self.name,self.age))

class Cat(Pet):
    def __init__(self,name,age,color):
        super().__init__(name,age) #calls the parent class init parameters
        self.color = color

    def speak(self):
        print("Meow")
    
    def my_color(self):
        print(f"My color is {self.color}")

class Dog(Pet):
    def __init__(self,name,age,color):
        super().__init__(name,age)
        self.color = color

    def speak(self):
        print("uugh")

    def my_color(self):
        print(f"My color is {self.color}")


# instance of pet class

my_pet  = Pet("Tim",5)
my_pet.show()
print()

my_cat = Cat("Japhine",50,"grey")
my_cat.show()
my_cat.my_color()
my_cat.speak()
print()

my_dog = Dog("Barack",16,"Brown")
my_dog.show()
my_dog.my_color()
my_dog.speak()


# Class attributes -- specific to a class
print("Class attributes -- specific to a class")
class Person:
    #used for constants
    num_of_people =0 #a class attribute

    def __init__(self,name):
        self.name = name
        Person.num_of_people += 1

p1 = Person("Collince")
print(Person.num_of_people)
print(p1.num_of_people)

p2 = Person("Kevin")
# p2.num_of_people = 5 explicite assigning num_of_people a value
# Person.num_of_people = 34 #changes the attribute to all except where specified explicitely

# print(p2.num_of_people) 
print(Person.num_of_people)


# CLASS METHODS
print("Class methods")
class Person:
    num_of_people =0 
    gravity = -9.8 #m/s**2

    def __init__(self,name):
        self.name = name
        Person.add_person()
    
    @classmethod #a class method decorator, called on the class itself
    #the class is not going to act on one instance
    def num_of_people_(cls): #cls - class
        return cls.num_of_people
    
    @classmethod
    def add_person(cls):
        cls.num_of_people += 1

p1 = Person("Person 1")
p2 = Person("Person 2")
p3 = Person("Person 3")
# p4 = Person("Person 4")
print("Class method num of people",Person.num_of_people_())


# STATIC METHODS

class Math:
    @staticmethod #they do something but doesn't change
    def add5(x):
        return x + 5
    
    @staticmethod
    def add50(x):
        return x + 50
    
    @staticmethod
    def add500(x):
        return x + 500
    
    @staticmethod
    def pr():
        return "run"

print()
print(Math.add500(34))
print(Math.pr())

print("\n\n")
print("Working with an instance you'll use self\nWorking with a class you use cls(class)")





#Telusko tutorial
class Laptop:
    laptop_brand = "HP Elitebook 840 G5" #class variable

    def __init__(self,cpu,memory,storage): #self...instance method works with instance variables
        self.cpu = cpu
        self.memory = memory
        self.storage = storage

    def config(self):
        print("i5, 16GB, 512SSD, 14\"")
    
    def show_cpu(self):
        print(self.cpu)

    def compare(self,other):
        if self.memory == other.memory:
            return True
        else:
            return False
    
    def get_storage(self): #accessor method, 'getters'
        return self.storage
    
    def set_storage(self,value): #mutator method 'setters'
        self.storage = value

    @classmethod #class method...works with class
    def my_brand(cls):
        return cls.laptop_brand

    @staticmethod   #static method...works with nothing
    def info():
        print("This is a static method")

com1 = Laptop("i5", "16GB", "512SSD")
com2 = Laptop("i5", "8GB", "512SSD")
com1.show_cpu()
print("#shows the address of the memory where object com1 is stored")
print("Address of com1:",id(com1)) 
print("Address of com2:",id(com2))
print()
if com1.compare(com2):
    print("com1 and com2 have the same memory size")
else:
    print(f"Different memory size, com1 {com1.memory} and com2 {com2.memory}")

print("instance variable works with the objects")
print("accessor methods: used when just fetching the values of instance variables")
print("mutator methods: used when modifying the values of instance variable")

print(Laptop.my_brand())
com1.info()


print("\n\nClass inside another class")

class Student:
    def __init__(self,name,admno):
        self.name = name
        self.admnno = admno
        self.lap = self.New_Laptop() #calling the inner class from within the outer class

    def show(self):
        print(f"Student name {self.name} and admission no {self.admnno}")
        self.lap.show()
    #Inner class, Laptop is a inner class of Students class
    class New_Laptop: 
        def __init__(self):
            self.new_brand = "HP"
            self.new_cpu = "i5"
            self.new_ram = "8GB"
            self.speed = "3.6GHZ"

        def show(self):
            print(f"Laptop Details\nBrand: {self.new_brand}\nProcessor: {self.new_cpu}\nRAM: {self.new_ram}")

 #calling the inner class from outside, you must use the outer class name ten dot inner class
out_laptop = Student.New_Laptop()

lap2 = Student.New_Laptop()#calling the inner class from outside the outer class provided you use the outer class name to call it
s1 =Student("Collince",200)
s1.show()
print()
s1.lap.show()
print("Speed",out_laptop.speed)


#INHERITANCE
print()

class A: #supper class
    def feature1(self):
        print("Feature 1 working")

    def feature2(self):
        print("Feature 2 working")

class Thigammy():
    def ambiguous(self):
        print("Ambiguous class")

class B(A): #child class / a sub class....single level inheritance
    def feature3(self):
        print("Feature 3 working")

    def feature4(self):
        print("Feature 4 working")


class C(B): # multilevel inheritance...grandchild    
    def feature5(self):
        print("Feature 5 working")

class D():
    def show(self):
        print("Cheking whether it throws an error")

class D(Thigammy,C): # multiple inheritance...inherit from two or more different classes which are not related    
    def featureD(self):
        print("Feature D working")

a1 = A()
a1.feature1()
a1.feature2() 

b1 = B()
print()
b1.feature3()
b1.feature4()
b1.feature1()
b1.feature2()

c1 = C()
c1.feature1()

d1 = D()
d1.featureD()
d1.ambiguous()
print()

#CONSTRUCTOR
print()

class A: #supper class
    
    def __init__(self): #a constructor
        print("In class A init")

    def feature1(self):
        print("Feature 1-A working")

    def feature2(self):
        print("Feature 2 working")

class B(A): #child class / a sub class....single level inheritance
    def __init__(self):
        super().__init__()#enable class B to call the init in A
        print("in class B init")

    def feature1(self):
        print("Feature 1-B working")

    def feature4(self):
        print("Feature 4 working")

class Ambig():
    def __init__(self): #a constructor
        print("In class Ambig init")

    def ambiguity(self):
        print("Ambiguous class")

class C(A,Ambig):

    def __init__(self): #a constructor
        super().__init__()
        print("In class C init")

    def feature1(self):
        super().feature2()

    def feature3(self):
        print("Feature c working")

#by default, a class calls it's own init, if it's not 
# available then it chacks from the supper class
# A() 
# B() #without the init in B and without the super().__init__(), it'll call the init in A coz of inheritance
# super().__init__() will call the init of the super class then call the init of the class


# with MRO method resolution order, calling classes or 
# functions start from left to right
class_c = C()
class_c.feature1()


#POLYMORPHISM
# 1 duck typing
# 2 operator overloading
# 3 method overloading
# 4 method overriding
print()
print("POLYMORPHISM")

#1 duck typing
class PyCharm():
    def execute(self):
        print("Compiling")
        print("Running")

class MyEditor():
    def execute(self):
        print("Convention check")
        print("Compiling")
        print("Running")

class Laptop():
    def code(self,ide):
        ide.execute()
        
ide = MyEditor()

lap = Laptop()
lap.code(ide)

print()

# 2 operator overloading
a =50
b = 20

print(a+b) #the + sign calls int.__add__(a,b) behind the scene, the two nums are of int type, the int class has a add function
print(int.__add__(a,b))
print(str.__add__(f"{a}",f"{b}")) #str also have a add method

# + calls __add__ method
# - calls __sub__ method
# * calls __mul__ method 
# / calls __div__ method 
# < calls __lt__ method 
# > calls __ge__ method 
# >= calls __ge__ method 
# <= calls __le__ method etc

class Candidate:
    def __init__(self,m1,m2):
        self.m1 = m1
        self.m2 = m2

    def __add__(self,other): #overloading __add__
        m1 = self.m1 + other.m1
        m2 = self.m2 + other.m2
        sd3 = Candidate(m1,m2)
        return sd3
    
    #gt greater than....ge greater than or equal to
    def __gt__(self, other):
        r1 = self.m1 + self.m2
        r2 = other.m1 + other.m2

        if r1 > r2:
            return True
        else:
            return False

    def __str__(self):
        # return self.m1,self.m2
        return f"{self.m1}, {self.m2}"

sd1 = Candidate(50,60)
sd2 = Candidate(54,48)
sd3 = sd1 + sd2 #gets converted to Candidate.__add__(sd1,sd2) then calls the overloaded add
print("Total m1 for candidates",sd3.m1)
print("Total m2 for candidates",sd3.m2)

if sd1 > sd2: #calls the overloaded greater than method __gt__
    print("Sd1 wins")
else:
    print("Sd2 wins")

a = 9
print(a)# calls a.__str__(), same as below
print(a.__str__()) 

print(sd1)
print(sd1.__str__()) #prints the addres of sd1 if the method is not overloaded
print(sd2.__str__())
print(sd2)

print()


# 3 method overloading --> two method of the same name but different num of parameters, not available in python
# 4 method overriding  --> two methods with same name and same num of parameters

# method overloading

class Overloading_class:
    def __init__(self,m1,m2):
        self.m1 = m1
        self.m2 = m2

    def sum(self):
        return self.m1 + self.m2
    
    def anotherSum(self,*a):

    #example of method overloading using the same +,...a trick in python
    # def anotherSum(self,a=None,b=None,c=None):
        s= 0
        # if a!=None and b!=None and c!=None:
        #     s = a+b+c
        # elif a!=None and b!=None:
        #     s = a+b
        # else:
        #     s = a

        for val in a:
            s += val
        return s
    
    def __str__(self):
        # pass
        return f"{self.m1}, {self.m2}"
        
    
cs = Overloading_class(5,18)
print(cs) #overloaded the __str__ to print the values
print(cs.sum())

print(cs.anotherSum(45,200,45,46,454,45,3,43))

print()


#METHOD OVERRIDING

class Overr_A:
    def show(self):
        print("in overr_A show")

class Overr_B(Overr_A):
    def show(self): #this show overrides the parent class show
        print("in overr_B show")




overcls = Overr_B()
overcls.show()


def One():
    print("Function one")
def Two():
    print("Function two")
def Three():
    print("Function three")

my_ops = {"One":One,"Two":Two,"Three":Three}
my_list = list(my_ops)
num = 1

def call_func(func): 
    try:
        return my_ops[func]()
    except:
        return "Invalid function"

selected_func = my_list[1]
call_func(selected_func)