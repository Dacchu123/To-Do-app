feet_inches = input("Enter feet and inches : ")


def parse(feet_inches):
    parts = feet_inches.split(" ")
    feet = float(parts[0])
    inches = float(parts[1])
    return {'feet': feet, 'inches': inches}


def convert(feet, inches):
    meter = feet * 0.3048 + inches * 0.0254
    return meter


parsed = parse(feet_inches)
result = convert(parsed['feet'], parsed['inches'])
print(f"feet: {parsed['feet']} and inches: {parsed['inches']} are equal to {result}")

if result >= 1:
    print("children play games")

else:
    print("children not play game")
