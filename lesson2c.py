#Dictionary Data Types
#A dictionary is a data type that stores its data in form of key-value pairs
#it is introduced by use of curly braces{}
#The va;lues stored inside of a dictionary can be ofdifferent data types. ie;int, tuple, sting, list,dictionary
#Note: unlike tupples and lists, on the dictionary we normally use the keys to acces the values.
#The keys and the values are separated by the use of full colon
#At the end of each pair there should be a comma

 
#example one
phonebook = {
    "Benson" : 254789098766,
    "Mary" : 2540987654432,
    "Joseph" : 25431125654
}
print("My dictionary is", phonebook)
print(type(phonebook))

#Below we use the keys to access items of the dictionary
print(phonebook["Benson"])
print(phonebook["Mary"])

print("=============================================")

player = {
    "name" : "Messi",
    "age" : 40,
    "teams" : ["Miami","PSG", "Bacelona", "Argentina"],
    "more" : {
        "children" : 3,
        "residence" : "US",
        "number" : (10829834743, 9897326875, 1234567899)
    }
}

print(player["name"])
print(player["teams"][2])
print(player["more"]["number"][1])