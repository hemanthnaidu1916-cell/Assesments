print("Pronic numbers between 1 and 100:")

for i in range(1, 100):
    p = i * (i + 1)
    if p <= 100:
        print(p, end=" | ")
