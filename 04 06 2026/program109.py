def num_layers(n):
    thickness_mm = 0.5 * (2 ** n)
    thickness_m = thickness_mm / 1000
    return str(thickness_m) + "m"

print(num_layers(1))
print(num_layers(4))
print(num_layers(21))
