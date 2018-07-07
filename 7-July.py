

class Student:
    name = ""
    college = ""
    fees = 0

    def __init__(self, name = "", college = "", fees = 0):
        self.name = name
        self.college = college
        self.fees = fees

list=[]

obj = Student("Gurjas", "DIT", 8000)
obj1 = Student("Kunal", "DIT", 8000)
obj2 = Student("Piyush", "DIT", 8000)
list.append(obj)
list.append(obj1)
list.append(obj2)

for i in list:
    print("Student Name is: ", i.name, ", Student College is: ", i.college, ", Student Fees is: ", i.fees)









    
