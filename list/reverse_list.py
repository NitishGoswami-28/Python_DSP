import random
upper= random.randint(1, 10)
arr = random.sample(range(100), upper)
print("OG list:",arr)
new = arr[::-1]
print("New list: ", new)