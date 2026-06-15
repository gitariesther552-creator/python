# Create a python program that is able to calculate the simple interest given the principle as 50000, rate as 5% and time as 8 years. SI = (p * R * t)/100



# Assignment
# 1. Write a python program that is able to calculate the BMI of a person whose weight is 78kgs and height is 1.75 meters. BMI = (weight) / (height squared)
# 2. Find the Area and perimeter of a rectangle whose length is 48cm and width is 25cm
# Research on python list, tuple and Dictionary Data types.

#question one
p = 50000
r = 5
t = 8
i = p * r * t
si = i / 100
print("the answer is", si)

#question two
w = 78
h = 1.75
exponent = h ** 2
bmi = w / exponent
print("the answer is ", bmi)

#question three 
le = 48
wi = 25
#area
area = le * wi
print(area)

#perimeter
perimeter = (le + wi) *2
print(perimeter)
