#Based on the if..elif..else conditional statement you can create the grading system as shown below


marks = 47

if marks > 0 and marks < 30:
    print("The grade attained is: Ë")
elif marks >=30 and marks < 50:
    print("The grade attained is: D")
elif marks >=50 and marks < 60:
    print("The grade attained is: C")
elif marks >=60 and marks < 70:
    print("The grade attained is: B")
elif marks >=70 and marks < 100:
    print("The grade attained is: A")
else:
    print("Invalid entry. please try again...")
    

print("=============================")
#JOhn want to donate blood but there is a condition he need to check. a person who can be able to donate blood is that who has attained 50kgs or above and his/her age is not less than 18. create a python program that is able to check whether John who has 57kgs and 26years of age is able to donate blood.

name = "John"
weight = 57
age = 26

if age >= 18 and weight >= 50:
    print("Can donate blood")
else:
    print("Cannot donate blood")
    
