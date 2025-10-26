#A set stores unique elements (no duplicates).

numbers = { 1 ,2 , 3 , 4 , 4 , 5}
print(numbers)

numbers.add(6)

numbers.remove(3)

print(numbers)

A = {1,2,3,4,5}
B = {3,4,5,6,7}

print("Union:" , A|B)
print("Intersection:", A & B)
print("Difference:", A - B)    