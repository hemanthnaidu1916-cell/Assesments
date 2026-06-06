lists = [[1, 2, 3], [],[4,5], [], [6, 7, 6], []]
result = []

for item in lists:
    if item != []:
        result.append(item)

print(result)
