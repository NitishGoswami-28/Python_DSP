n = int(input("Enter the position: "))

fib_seq =[0,1]
while len(fib_seq) < n:
    nxt_num = fib_seq[-1] + fib_seq[-2]
    fib_seq.append(nxt_num)
print("The Fibonnaci number is: ", fib_seq[-1])
    