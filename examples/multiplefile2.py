filename = ['a.txt', 'b.txt', 'c.txt']

for filenames in filename:
    file = open(f'../bonus/files/{filenames}', 'r')
    content = file.read()
    print(content)
    file.close()
