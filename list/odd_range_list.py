import random
rng = int(input("Enter the range: "))
print("The odd numbers are:")
for i in range(rng):
    if i%2 != 0:
        print(i,end=" ")