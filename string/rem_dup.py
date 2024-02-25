def remove_duplicates(input_str):

    unique_chars = set()
    result = []

    for char in input_str:
        if char not in unique_chars:
            unique_chars.add(char)
            result.append(char)

    return ''.join(result)

input_string = str(input("Enter string: "))

result_string = remove_duplicates(input_string)
print("Removing duplicates:", result_string)
