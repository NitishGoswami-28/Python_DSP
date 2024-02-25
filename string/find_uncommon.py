def find_uncommon_words(str1, str2):
    words1 = set(str1.split())
    words2 = set(str2.split())

    uncommon_words = words1.symmetric_difference(words2)

    return uncommon_words

# Example usage:
string1 = str(input("Enter string1: "))
string2 = str(input("Enter string2: "))

result = find_uncommon_words(string1, string2)
print("Uncommon words:", result)
