#Functions Assignment 
# 1. Create a Function to Find Simple Interest – PRT/100 
# 2. Create a Function to Find Area of a Triangle – 1/2bh.
# – (With Parameters)


#Question one
#principal = 1500
#rate = 10/100
#time = 6

def interest(principal, rate, time):
    simpleinterest = principal * rate * time
    print("The answer is:", simpleinterest)
    
interest(1500, 10/100, 6)

# 2. Create a Function to Find Area of a Triangle – 1/2bh.

def area(b, h):
    areatriangle =  (b * h)/2
    print("The answer is:",areatriangle)
    
area(60, 80)
    