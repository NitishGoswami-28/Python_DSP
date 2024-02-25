def remove_empty_lists(lst):
    lst = [sublist for sublist in lst if sublist]
    return lst

my_list = [1, [], 3, [], 5, [], 7]
result_list = remove_empty_lists(my_list)
print("List after removal:", result_list)
