def is_binary_str(s):
    return all(c in '01' for c in s)

input_str = "1001110"

if is_binary_str(input_str):
    print(f"'{input_str}' is a binary string.")
else:
    print(f"'{input_str}' is not a binary string.")
