name = "Anubhav Dwivedi"
greeting = "Hello " + name
print(greeting)

#Indexing and Slicing

print(name[0]) # First Character
print(name[-1]) # Second Character
print(name[0:7]) #slice

#String methods

print(name.upper())
print(name.lower())
print(name.replace("Dwivedi" , "Kailash")) #changes are made in copy of the string
print(name.split())

#Loop through string

for char in name:
    print(char, end=" ")






