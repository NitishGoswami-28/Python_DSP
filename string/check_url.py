def check_url(input_str):
    input_lower = input_str.lower()
    url_prefixes = ['http://', 'https://', 'www.']
    
    for prefix in url_prefixes:
        if prefix in input_str_lower:
            return True

    return False


input_str = str(input("Enter a string: "))

if check_url(input_str):
    print("URL found in the string.")
else:
    print("No URL found in the string.")