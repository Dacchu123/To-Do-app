import csv

with open("../Dailyuse/weather.csv", 'r') as files:
    data = list(csv.reader(files))

city = input("Enter your city: ")

for row in data:
    if row[0] == city:
        print(row[1])
