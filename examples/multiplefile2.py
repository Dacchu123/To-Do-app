filename = ['a.txt','b.txt','c.txt']

for filenames in filename:
    file = open(f'./files/{filenames}', 'r')
    content = file.read()
    print(content)
    file.close()
