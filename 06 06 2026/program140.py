def vow_replace(string, vowel):
    vowels = "aeiou"
    return "".join(vowel if ch in vowels else ch for ch in string)
print(vow_replace("apples and bananas", "u"))

print(vow_replace("cheese casserole", "o"))

print(vow_replace("stuffed jalapeno poppers", "e"))
