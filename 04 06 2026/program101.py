def hamming_distance(s1, s2):
    if len(s1) != len(s2):
        return "Strings must be of equal length"

    count = 0
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            count += 1

    return count


print(hamming_distance("abcde", "bcdef"))
print(hamming_distance("abcde", "abcde"))
print(hamming_distance("strong", "strung"))
