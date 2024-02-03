tuple_of_lists = ([1, 2, 3], ['a', 'b'], [4, 5])

flattened_tuple = tuple(item for sublist in tuple_of_lists for item in sublist)

print("Original tuple of lists:", tuple_of_lists)
print("Flattened tuple:", flattened_tuple)
