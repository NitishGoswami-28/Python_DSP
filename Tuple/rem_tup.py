
tuple_list = [(1, 2, 3), ('a', 'b'), (4, 5, 6), ('x', 'y', 'z')]
k_len = 3
tuples =[tpl for tpl in tuple_list if len(tpl) != k_len]

print("Original tuple list:", tuple_list)
print(f"Tuples of length {k_len} removed:", tuples)
