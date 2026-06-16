#Python Tuples
#A tuple is a type of a list that is not mutable(unchangeable)
#To introduce atuple, we use the parenthesis/brackets ()

counties = ("Nairobi", "Machakos", "Kisumu", "Kisii", "Narok", "Mombasa", "Lamu", "Kilifi")
print(counties)
print(type(counties))

#A tuple stores its items on indexes
# We also starts from index zero onwards
print(counties[3])

#Slicing of Tuples
print(counties[3:])

print(counties[1:6])

#note; below code will show an error because atuple is immutable
counties.append("Nakuru")
print(counties)