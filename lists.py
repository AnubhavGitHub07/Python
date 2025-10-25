fruits = ["apple" , "banana" , "cherry"]

print(fruits[0])
print(fruits[-1])

fruits.append("mango")
fruits.insert(1, "grapes")
print(fruits)

fruits.remove("banana")
popped = fruits.pop()
print(fruits)
print("Popped : " , popped)

for fruit in fruits:
    print(fruit)

squares = [ x**2 for x in range(1,6)]
print(squares)