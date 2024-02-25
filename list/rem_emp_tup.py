def remove_empty_tuples(lst):
    lst = [tup for tup in lst if tup]
    return lst

my_list = [(1, 2), (), (3, 4), (), (5, 6)]
result_list = remove_empty_tuples(my_list)
print("List after removal:", result_list)
