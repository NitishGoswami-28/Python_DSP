tuple_list = [(1, 5), (3, 2), (2, 8), (4, 3)]

sorted_tuples = sorted(tuple_list, key=lambda x: x[1])

print("Original tuple list:", tuple_list)
print("Sorted tuples by second item:", sorted_tuples)
