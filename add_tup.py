# Adding Tuple to List
def tuple_to_list(lis, tup):
    lis.append(tup)
    return lis

# Adding List to Tuple
def list_to_tuple(tup, lis):
    new_tuple = tup + tuple(lis)
    return new_tuple

og_list = [(1, 2), (3, 4), (5, 6)]
new_tup = (7, 8)

og_tup = (1, 2, 3)
new_lis = [4, 5, 6]

new_list = tuple_to_list(og_list, new_tup)
new_tuple = list_to_tuple(og_tup, new_lis)

print("List after adding tuple:")
print(new_list)

print("Tuple after adding list:")
print(new_tuple)