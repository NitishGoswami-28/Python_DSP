input_string = str(input("Enter string:"))

length_method_1 = len(input_string)

length_method_2 = 0
for char in input_string:
    length_method_2 += 1


length_method_3 = input_string.count('')
length_method_4 = sum(1 for _ in enumerate(input_string, 1))

print("Method 4 - Using enumerate() and counting:", length_method_4)
print("Method 3 - Using count():", length_method_3 - 1)
print("Method 2 - Iterating through characters:", length_method_2)
print("Method 1 - Using len():", length_method_1)
