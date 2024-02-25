start = int(input("Enter the start range (-ve): "))
end = int(input("Enter the end range: "))
for num in range(start, end + 1):
    if num < 0:
        print(num)