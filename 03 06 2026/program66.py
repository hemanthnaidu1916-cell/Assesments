string = input("Enter a string: ")

special_chars = "!@#$%^&*()-+?_=,<>/"

found = False

for char in string:
    if char in special_chars:
        found = True
        break

if found:
    print("The string contains special character(s).")
else:
    print("The string does not contain any special characters.")
