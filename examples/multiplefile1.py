content = ["Hello", "Hello", "Hello"]

filenames = ['doc.txt', 'report.txt', 'presentation.txt']

for i, j in zip(content, filenames):
    file = open(f'../bonus/files/{j}', 'w')
    file.write(i)
    file.close()
