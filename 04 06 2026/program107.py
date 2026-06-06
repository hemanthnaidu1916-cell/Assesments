def double_char(text):
    return "".join(char * 2 for char in text)

print(double_char("String"))
print(double_char("Hello World!"))
print(double_char("1234! "))
