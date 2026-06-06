def ascii_capitalize(s):
    return "".join(
        ch.upper() if ord(ch) % 2 == 0 else ch.lower()
        for ch in s
    )
print(ascii_capitalize("to be or not to be!"))

print(ascii_capitalize("THE LITTLE MERMAID"))

print(ascii_capitalize("Oh what a beautiful morning."))
