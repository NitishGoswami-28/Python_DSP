p = float(input("Enter the Principal:"))
r = float(input("Enter the rate of interest: "))
t = int(input("Enter the time duration in years: "))
n = int(input("Enter the number of times compounding happens: "))

ci = p * (1 + r / n) ** (n * t)

print(f"The Compound Interest is: {ci:.2f}")