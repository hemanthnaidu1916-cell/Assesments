words = input("Enter words: ").split()

unique_words = sorted(set(words))

print(" ".join(unique_words))
