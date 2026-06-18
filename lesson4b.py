#python functions with parametrs
#parameters are valuews that get passed as arguements when you invole a function


def greeting(name):
    print(f"hello hope youre doing fine")
    
greeting("Joan")
greeting("Peter")
greeting("Jane")
greeting("Mirriam")


print("=============================")
#below is an addition function that accepts three parameters
def add(x , y , z):
    sum = x + y + z
    print("The sum of the number is:", sum)
    
#below we invoke/ call our function
add(45, 20, 16)
add(10, 15 ,5)

print("=============================")
#by use of a function that accepts parameters, calculate the speed of a vihecle which covered 400km in 5 hours time. speed = distance / time

def divide(dis , time):
    speed = dis / time
    print("the answer is:", speed)
    
divide(400 , 5)
