password = input("Enter new password: ")

result = []

if len(password) >= 8:
    result.append(True)
else:
    result.append(False)

digit = False
for i in password:
    if i.isdigit():
        digit = True

result.append(digit)

uppercase = False
for i in password:
    if i.isupper():
        uppercase = True

result.append(uppercase)

# special = False
# for i in password:
#     if i.isascii():
#         special = True
#
# result.append(special)

if all(result):
    print("Strong Password")
else:
    print("Weak password")
