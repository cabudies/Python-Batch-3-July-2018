# use input() function to take input from user
# use int() function to convert string to int
number = int(input('Enter the number of rows for star pattern: '))

for i in range(0, number):
    for j in range(0, i):
        print("*", end=" ")
    print()

# use def to create a function
def printUserDetails():
    print("hello")
    a = 10
    return a
    
name = input("Hello enter your name: ")
age = int(input("Enter your age: "))

# calling a function using it's name.
number = printUserDetails()
print(number)

