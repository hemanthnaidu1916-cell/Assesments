def society_name(names):
    return ''.join(sorted(name[0] for name in names))
print(society_name(["Adam", "Sarah", "Malcolm"]))

print(society_name(["Harry", "Newt", "Luna", "Cho"]))

