import random
upper= random.randint(1, 10)
arr = random.sample(range(100), upper)
print("OG list:",arr)

for i in arr:
    if i%2 == 0:
        print(i,end=" ")