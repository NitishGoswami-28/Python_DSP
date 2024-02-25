def replace_str(input_str, old, new):
    return input_str.replace(old, new)


og = str(input("Enter the string: "))
old = str(input("Enter the substring to replace: "))
new = str(input("Enter the new substring to replace: "))

result = replace_str(og, old, new)
print(f"String after replacing '{old}' with '{new}':", result)
