import random
rng = int(input("Enter the range: "))
print("The even numbers are:")
for i in range(rng):
    if i%2 == 0:
        print(i,end=" ")