import glob

myfiles = glob.glob('../files/*.txt')

for filepath in myfiles:
    with open(filepath, 'r') as files:
        print(files.read())
