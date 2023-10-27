contents = ['All carrots are the sliced longitudinally', 'You are so amazing', 'Your look so gorgeous']

filenames = ['todo1.txt', 'todo2.txt', 'todo3.txt']

for content, filename in zip(contents, filenames):
    file = open(f'./files/{filename}', 'w')
    file.write(content)
    file.close()
