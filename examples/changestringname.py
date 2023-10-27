# Using list comperhensions to change string names

filenames = ['1.doc', '2.presentation', '3.report']

filenames = [filename.replace('.', '-', 1) + '.txt' for filename in filenames]

print(filenames)
