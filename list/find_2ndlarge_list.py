import random
upper= random.randint(1, 10)
arr = random.sample(range(100), upper)
print("OG list:",arr)

arr.sort(reverse=True)
print("The Second largest is: ", arr[1])