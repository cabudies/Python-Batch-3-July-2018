# inheritance example


# class BaseClass:
#     firstNumber = 10
#     secondNumber = 20
#
#     def __init__(self):
#         thirdNumber = self.firstNumber + self.secondNumber
#         print("Sum of two numbers is: %d" % (thirdNumber))
#
# class DerivedClass(BaseClass):
#
#     def __init__(self):
#         super(DerivedClass, self).__init__()
#
# obj = DerivedClass()









# Calling base class constructor and passing variables from base class
# Function overriding
# class BaseClass:
#     firstNumber = 10
#     secondNumber = 20
#
#     def __init__(self, firstNumber, secondNumber):
#         self.firstNumber = firstNumber
#         self.secondNumber = secondNumber
#         thirdNumber = self.firstNumber + self.secondNumber
#         print("Sum of two numbers is: %d" % (thirdNumber))
#
# class DerivedClass(BaseClass):
#
#     def __init__(self, firstNumber, secondNumber):
#         super(DerivedClass, self).__init__(firstNumber, secondNumber)
#
# obj = DerivedClass(30, 40)












# Multiple Inheritance
# class BaseClass2:
#     secondNumber = 20
#
#     def __init__(self, secondNumber):
#         self.secondNumber = secondNumber
#         print("Base Class 2")
#
# class BaseClass1:
#     firstNumber = 10
#
#     def __init__(self, firstNumber):
#         self.firstNumber = firstNumber
#         print("Base Class 1")
#
# class DerivedClass(BaseClass2, BaseClass1):
#
#     def __init__(self, firstNumber, secondNumber):
#         print("Derived Class")
#         BaseClass1.__init__(self, firstNumber)
#         BaseClass2.__init__(self, secondNumber)
#         thirdNumber = BaseClass1.firstNumber + BaseClass2.secondNumber
#         print("Total sum is: %d" % (thirdNumber))
#
# obj = DerivedClass(30, 40)