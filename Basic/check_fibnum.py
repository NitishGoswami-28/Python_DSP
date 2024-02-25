import math

num = int(input("Enter the number: "))

def check(number):
    root = math.sqrt(number)
    return root**2 == number

con1 = check((5* num**2 +4))
con2 = check((5* num**2 -4))

if con1 or con2:
    print("It is a fibonnaci number")
else:
    print("It is not")