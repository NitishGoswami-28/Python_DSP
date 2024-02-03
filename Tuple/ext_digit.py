def extract_digits(tuple_list):
    digits = []

    for tpl in tuple_list:
        for item in tpl:
            if isinstance(item, int):
                digits.append(item)

    return digits


tuple_list = [(1, 'apple', 23), (2, 'banana', 45), (3, 'orange', '56'), ('kiwi', 78)]

result_digits = extract_digits(tuple_list)

    
    
    
print("Original tuple list:", tuple_list)
print("Extracted digits:", result_digits)
