#creating a dictionary

student = {
    "name" : "Anubhav Dwivedi",
    "age" : 20,
    "course" : "B.tech AIML"
}

#Accessing values

print(student["name"])

# Adding a new key-value pair

student["grade"] = "A"

# Looping through dictionary
for key, value in student.items():
    print(key, ":", value)

# Checking if key exists
if "age" in student:
    print("Age Exist")

# Removing an item
student.pop("course")
print(student)