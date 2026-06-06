def index_of_caps(text):
    return [i for i, ch in enumerate(text) if ch.isupper()]

print(index_of_caps("eDaBiT"))
print(index_of_caps("eQuINoX"))
print(index_of_caps("determine"))
print(index_of_caps("STRIKE"))
print(index_of_caps("sUn"))
