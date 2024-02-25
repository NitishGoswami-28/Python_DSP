number = int(input("Enter the number"))

arm = lambda x: (x%10) if (x/10) ==0 else (x%10)**3 + arm(x//10)

if arm(number) == number: 
    print("It is armstrong")
else: 
    print("it is not armstrong")
