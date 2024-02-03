
    
tup = (3, 1, 4, 1, 5, 9, 6, 5, 3, 5)
k = 3
sorted_tuple = sorted(tup)
max_elements = sorted_tuple[-k:]
min_elements = sorted_tuple[:k]

print(f"Maximum {k} elements: {max_elements}")
print(f"Minimum {k} elements: {min_elements}")
