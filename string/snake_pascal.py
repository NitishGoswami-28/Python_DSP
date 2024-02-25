snake = str(input("Enter snake_case: "))
words = snake.split('_')
pascal = ''.join(word.capitalize() for word in words)
print("PascalCase: ",pascal)