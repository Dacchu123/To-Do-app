date = input("Enter today's date : ")
mood = input("How do you rate your mood today from 1 to 10 ?? ")
thoughts = input("Let your thoughts flow : ")
opinion = input("Let tell me your opinion : ")

with open(f'../bonus/files/{date}.txt', 'w') as files:
    files.write(f'Rating = {mood}\n')
    files.write(f'thoughts = {thoughts}\n')
    files.write(f"opinion = {opinion}\n\n")

print("Have a good day ")
