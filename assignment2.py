#when age is less than 10 the program should print “You are in Primary Classes” when age more 12 and less than 15 the program should print “You are in Junior Secondary” when age > 15 and less than 19 the program should print “You are in Senior Secondary” when age > 19 the program should print “You are

age = 18

if age < 10:
    print("You are in primary school")
elif age >12 and age <15:
    print("You are in junior school")
elif age >15 and age <19:
    print("You are in senior secondary")
else:
    print("You are in university")
    
    
    
# By use of a for loop, find all the leap years in between the year 2000 and 2030
for leap_years in range(2000,2030,4):
    print(leap_years)
    
    

# Assignment: Create a tuple of languages with 10 international languages. If English is found on the tuple, terminate the loop and print("English is found") otherwise print("English is not found")
languages = ("french","arabic", "hindi","portugues","russian","english","german","japanese")
print(languages)
for english in languages:
    print(english)