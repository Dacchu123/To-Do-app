f_i = input("Enter feet and inches : ")


def feet_inches(f_i):
    parts = f_i.split(" ")
    feet = float(parts[0])
    inches = float(parts[1])
    convert = feet * 0.3048 + inches * 0.0254
    return convert


result = feet_inches(f_i)

if result < 1:
    print("kids it is too small")
else:
    print("Kids use this value")
