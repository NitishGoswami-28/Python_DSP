word = str(input("Enter the string: "))
rem = int(input("Enter the postion to remove: "))
if 0 <= rem < len(word):
    new_word = word[:rem] + word[rem+1:]
    print("String after removing: ", new_word)
else:
    print("enter a valid position.")