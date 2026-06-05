def find_duplicates(s):
    char_count = {}
    duplicates = set()
    for char in s:
        if char != ' ':
            char_count[char] = char_count.get(char, 0) + 1
            if char_count[char] > 1:
                duplicates.add(char)
    return list(duplicates)

input_string = "hemanth dilse"
duplicate_chars = find_duplicates(input_string)
print("Duplicate characters:", duplicate_chars)
