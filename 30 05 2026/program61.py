def remove_char(s, i):
    return s[:i] + s[i+1:]

input_str = "Hello, wWorld!"
i = 7
new_str = remove_char(input_str, i)
print(f"Original String: {input_str}")
print(f"String after removing {i}th character : {new_str}")
