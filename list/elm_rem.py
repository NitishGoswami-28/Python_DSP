lst = [1, 2, 3, 4, 5, 6, 7]
elem_to_rem = [2, 4, 6]
res_lst = [elem for elem in lst if elem not in elem_to_rem]
print("List after removal:", res_lst)
