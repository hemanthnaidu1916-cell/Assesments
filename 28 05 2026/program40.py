sentence = input("Enter a sentence: ")
words = sentence.split()
words.sort()
print("Sorted words:")
for word in words:
    print(word)
