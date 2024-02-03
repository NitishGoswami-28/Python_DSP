tuple_list = [('a', 3), ('b', 1), ('c', 2)]
order_list = ['b', 'c', 'a']

ordered_tuples = sorted(tuple_list, key=lambda x: order_list.index(x[0]))

print("Original tuple list:", tuple_list)
print("External order list:", order_list)
print("Tuples ordered by external list:", ordered_tuples)
