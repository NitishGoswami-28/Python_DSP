word = str(input("Enter a word to check: "))
if word == word[::-1]:
    print("It's palindrome")
else:
    print("It's not palindrome")