import random
from functools import reduce


upper= random.randint(1, 10)
arr = random.sample(range(100), upper)
print("OG list:",arr)

def multiply(x, y):
    return x * y

product = reduce(multiply, arr)
print("product: ",product)
