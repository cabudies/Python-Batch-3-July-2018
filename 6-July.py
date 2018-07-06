def starPatternInverse():
    for i in range(0, 8):
        for j in range(i, 8):
            print("* ", end="")
        for k in range(0, i):
            print("  ", end="")
        if(i>0):
            for m in range(0, i):
                print("  ", end="")
        for n in range(8, i, -1):
            print("* ", end="")
        print()

def starPatternDiamond():
    for i in range(0, 8):
        if (i<5):
            for j in range(i, 5):
                print("  ", end="")
            for k in range(0, i):
                print("* ", end="")
            if(i>0):
                for m in range(0, i-1):
                    print("* ", end="")
            print()
        else:
            for j in range(5, i+2):
                print("  ", end="")
            for k in range(i, 8):
                print("* ", end="")
            if(i>4):
                for m in range(8, i+1, -1):
                    print("* ", end="")
            print()

starPatternInverse()
starPatternDiamond()

# How to write function in python
# How to pass variables in python
##def sumTwoNumbers(var1 = 0, var2 = 5):
##    var3 = var1 + var2
##    print(var3)
##
# taking input from user and converting it to int
##var1 = int(input("Enter value for variable 1: "))
##var2 = int(input("Enter value for variable 2: "))
##
# calling function.
###sumTwoNumbers(var1, var2)
##sumTwoNumbers(var1)

# defining class in python
class Student:
    # member variables in python
    name = 'Gurjas'
    college = 'DIT'

    # constructor in python and passing values to member variables
    def __init__(self, name):
        self.name = name

    # using self keyword while writing functions in python
    def printDetails(self):
        print("Details are as follows: ", self.name)

# using objects of a class in python.
# passing value to objects in python.
obj = Student('Mohit')
obj.printDetails()
        
