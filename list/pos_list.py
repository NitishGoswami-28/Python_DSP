import random
upper= random.randint(1, 10)
arr = random.sample(range(-100,100), upper)
print("OG list:",arr)

print("The positive numbers are: ")
for i in arr:
    if i>=0:
        print(i,end=" ")