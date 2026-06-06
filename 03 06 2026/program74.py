import math

C = 50
H = 30

D_values = input("Enter comma-separated values of D: ").split(',')

result = []

for D in D_values:
    Q = round(math.sqrt((2 * C * int(D)) / H))
    result.append(str(Q))

print(",".join(result))
