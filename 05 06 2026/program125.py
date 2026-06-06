def is_isogram(word):
    word = word.lower()
    return len(word) == len(set(word))
print(is_isogram("Algorism"))
print(is_isogram("PasSword"))

print(is_isogram("Consecutive"))
