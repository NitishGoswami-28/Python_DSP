def is_binary(input_str):
    valid_digits = {'0', '1'}
    return all(char in valid_digits for char in input_str)

string = str(input("Enter string: "))

print(f"{string} {is_binary(string)}")
