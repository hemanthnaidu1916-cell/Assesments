str1 = "apple banana mango"
str2 = "banana orange apple grapes"

words1 = str1.split()
words2 = str2.split()

uncommon = []

for word in words1:
    if word not in words2:
        uncommon.append(word)

for word in words2:
    if word not in words1:
        uncommon.append(word)

print("Uncommon words:", uncommon)
