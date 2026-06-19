#Python modules
#Anmodule in python is a python file that contains the python definations and stuctures
#Definations - may include variables, functions, loops,, e.t.c
#We need modules to separate a huge chunks of programs into smaller and manageable pices, which are easier to understand and work with.
#in python we have two main types of modules ; 1. the inbuilt module   2. the user defined modules

def add ():
    number1 = 20
    number2 = 50
    sum = number1 + number2
    print("The sum is:", sum)
    

print("=====================")
#Below is a function to find the difference of numbers
def subtract():
    numx = int(input("Enter the first number"))
    numy = int(input("Enter the second number"))
    difference = numx - numy
    print("The difference of the number is:", difference)
    
#A python function that is able to calculate the area of a square
def multiple():
    no_1 = int(input("first side"))
    no_2 = int(input("second side"))
    area = no_1 * no_2
    print("The area of the square is:",area)