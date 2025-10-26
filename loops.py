#for loop

for i in range(1,6):
    print(i)

#while loop
num = 1           #initialize num
while num<=5:     #condition
    print(num)    
    num+=1        #updation

#loop with break and continue 
for i in range(1,10):
    if i == 5:
        break
    if i == 3:
        continue
    print(i)