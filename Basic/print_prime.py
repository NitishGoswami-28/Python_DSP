def is_prime(number):
    
    if number <= 1:
        return False  
    
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False  
        
    return True 

rng = int(input("Enter the range: "))

if rng<=2:
    print("Prime Number do not exists in this range")
else:
    for i in range(2, rng):
        if is_prime(i):
            print(i)
