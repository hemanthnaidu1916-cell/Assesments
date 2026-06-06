import re

passwords = input("Enter comma-separated passwords: ").split(',')

valid_passwords = []

for pwd in passwords:
    pwd = pwd.strip()

    if (6 <= len(pwd) <= 12 and
        re.search(r'[a-z]', pwd) and
        re.search(r'[A-Z]', pwd) and
        re.search(r'[0-9]', pwd) and
        re.search(r'[$#@]', pwd)):

        valid_passwords.append(pwd)

print(",".join(valid_passwords))
