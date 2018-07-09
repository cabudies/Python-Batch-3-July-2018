class Student:
     name = ""
     college = ""
     fees = 0

     # creating constructor in python and passing parameters
     def __init__(self, name = "", college = "", fees = 0):
         self.name = name
         self.college = college
         self.fees = fees

     # creating function inside class
     # if we define a function in a class, we need to define self as the first argument
     # inside function, if we define fees = 0, then we don't need to pass any value while
     # making a call to the function
     def fun(self, fees):
         self.fees = fees
         print("Hello fees is: ", self.fees)

# declaring a function outside the class
def fun():
    print("outside class")

# creating an empty list
list=[]

# creating an object of a class
obj = Student()

# calling a class function using the fun keyword
obj.fun(8000)

# calling a function which is declared outside the class
fun()

# dynamically taking input from the user and entering the details
numberOfEntries = int(input("Enter the number of records you want to enter: "))

for i in range(0, numberOfEntries):
    print("Enter the details of %d record: " % (i))
    obj = Student()
    obj.name = input("Enter the name of the student: ")
    obj.college = input("Enter the name of the college: ")
    obj.fees = int(input("Enter the fees of the student: "))
    list.append(obj)

# printing the list items one by one
for i in list:
    print("Student name is: ", i.name)
    print("College name is: ", i.college)
    print("Fees is: ", i.fees)
    print("****************")

# statically, entering the student's data
obj = Student("Gurjas", "DIT", 8000)
obj1 = Student("Kunal", "DIT", 8000)
obj2 = Student("Piyush", "DIT", 8000)
list.append(obj)
list.append(obj1)
list.append(obj2)

for i in list:
    print("Student Name is: ", i.name, ", Student College is: ", i.college, ", Student Fees is: ", i.fees)


## Exception Handling
fullName = input("Enter your full name:")

try:
    age = int(input("Enter your age:"))
    age = age + 10
except ValueError:
    print("Enter only integer value in age. ")
