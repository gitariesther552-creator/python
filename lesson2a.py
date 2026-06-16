#Boolean data type
# a boolean is a data type that evaluates either true of false.

israining = False
print(israining)
print(type(israining))

paidloan = True
print(paidloan)
print(type(paidloan))

#Python Lists Data Types
# A list is a collection of items that are ordered in a certain way.
# A list in python is introduced by the use of square brackets[]
# The items of a list are stored inside of indexes. Note ;in programing, indexes start from index zero
# Alist is mutable

cars = ["BMW", "Benz", "Prado", "Probox","Hiance", "Mclaren", "Ranger", "Rover"]
print(cars)
print(type(cars))

# Acessing items of a list.
#We use indexes to access the items.

print("the car on index zero is",cars[0])
print("the car on index five is",cars[5])

#List Slicing
# This is creating alist from an already existing list
#example one
print(cars[4:])

#example two
print(cars[0:4])

#example three
print(cars[3:7])

#List mutability
# We use the append function to add an item to the list
cars.append("mercedes")
print(cars)

cars.append("Subaru")
print(cars)

#we use the pop function to remove an item out of the end list
cars.pop()
print(cars)

# We can replace an item on a certain index as shown below
cars[0] = "Pajero"
print(cars)

#Below we use the del function to delete an item on the list
del cars[4]
print(cars)

