from collections import OrderedDict

def check_order(input_string, pattern):
    dict_chars = OrderedDict.fromkeys(input_string)

    ptr = 0
    for key in dict_chars.keys():
        if ptr < len(pattern) and key == pattern[ptr]:
            ptr += 1

    return ptr == len(pattern)

input_string = "engineers rock"
pattern = "egr"

if check_order(input_string, pattern):
    print("The order of characters is maintained.")
else:
    print("The order of characters is not maintained.")
