import random
upper= random.randint(1, 10)
arr = random.sample(range(100), upper)
print("OG list:",arr)

arr.sort(reverse=True)

lar = int(input("Enter to check for n largest: "))
print(f"The {lar} largest element is:", arr[lar-1])