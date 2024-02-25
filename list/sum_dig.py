def sum_of_digits(lst):
    return [sum(map(int, str(num))) for num in lst]

my_list = [123, 45, 678, 9]
result_sum_digits = sum_of_digits(my_list)
print("Sum of digits in list:", result_sum_digits)
