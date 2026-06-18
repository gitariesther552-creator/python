# Comparison / Relation Operators
#This are operators that are used to compare/ relate different conditions and they usually evaluate to boolean value(false/true)

#They are six in total ie;(>,<,>=,<=,==,!=)

print(5>2)
print(5<2)
print(5>=2)
print(5<=2)
print(5==2)
print(5!=2)

#logic operations
#logic AND - This evaluates to true only if both or all of the conditions are true
print((5<2) and (5>3))

# Logic OR - This evaluates to true if one of the conditions is true
print((5<2) or (5>3))

#Logic NOT
#This is used to negate a statement/condition (if the answer is true it is negated to false and viseversa )
print(not(5>2))

print("==================")
#If else conditional statemensts
# This is a conditional statement that is used to evaluate a condition and if itnis met, the if block execute, otherwise tyhe else block gets executed.

number = -10

if number >0:
    print("The number is positive")
else:
    print("The number is positive")
    
    
print("==================")
#Create a program that is able to evaluate whether a number is an even number or an odd number.

number2 = 2
if number2 % 2 == 0:
    print("The number is even")
else:
    print("The number is odd")
    

print("============")
#If ...elif...else conditional statements
# We use the below to evaluate multiple conditions
mynumber = 7
if mynumber > 0:
    print("The number is positive")
elif mynumber == 0:
    print("The number is zero")
else :
    print("The number is negative")
    

print("============")

Age = 15
if Age >= 18:
    print("You can vote")
else:
    print("You cannot be allowed to vote")