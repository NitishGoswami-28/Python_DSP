import random

arr = random.sample(range(100), 30)
print(arr)

num = int(input("Enter the number to find: "))
if num in arr:
    print("It exist")
else:
    print("The number do not exists")