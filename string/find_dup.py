def find_dup(inp_str):
    seen = set()
    duplicates = []
    
    for char in inp_str:
        if char in seen:
            duplicates.append(char)
        else:
            seen.add(char)
    
    return duplicates

input_str = str(input("Enter string: "))
result = find_dup(input_str)

if result:
    print("Duplicate characters:", ', '.join(result))
else:
    print("No duplicate characters found.")
