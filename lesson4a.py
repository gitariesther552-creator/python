#pyton functions
#Afunction is ablock of codes/statements that performs a given task/actio/job
#They are reusable - calculating a function you can invoke it mutiple times.
#We have two main types of function in python ie; 
#1. inbuilt functions - they can preinstall with the python interpreter eg( print(), append(), sort(), pop())
#2. User defined functions - These are functions that have been created by the programmer himself , to create a user defined function. we use the def keyword followed by the name of the function, parenthesis and a full colon at the end . on the line that follows,you need to indent which marks the body of the function


def greetings():
    print("hello ther hope you're doing fine,")

#below we invoke or call our function by use of its name    
greetings()



#below is an additional function
def addition():
    number1 = 30
    number2 = 20 
    answer = number1 + number2
    print("The number is:", answer)
    
addition()

print("=============================")
#create a function that is able to multiply three numbers, invokethe function to get the answer
def multiply():
    no1 =3
    no2 =4
    no3 =5
    answer = no1 * no2 * no3
    print("The number is:", answer)
    
multiply()


print("=============================")
#Below is a function that accepts user inputs
def divide():
    number1 = int(input("Enter the first number: "))
    number2 = int(input("Enter the second number: "))
    quotient = number1 / number2
    print("The answer is: ", quotient)
    
divide()
divide()
divide()