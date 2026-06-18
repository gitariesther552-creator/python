#Python loops
# Sometimes we may need to do a piece of codes a number of times and in such a case a loop may be of importance
#a loop is a control structure that allows us to execute a block of codes repaatedly until acondition is met.
#in python wehave two main types of loops ie; the for loop and the while loop

#python for loop
"""
for valuable in range(n):
     block of codes to be executed
"""

for greeting in range(10):
    print("Hello there", greeting)
    

print("========================")
for number in range(10, 20):
    print(number)
    

print("========================")
#Below we use some steps
for x in range (50,70,2):
    print(x)
    
print("========================")
# a program that is able to print all the odd numbers between zero and 51
for number in range (0,51,2):
    print(number)

