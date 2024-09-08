from sys import argv
import os

path = '.'
if(len(argv) > 1):
    path = argv[1]

os.makedirs(path, exist_ok=True)

with open('notExist.txt', 'r') as file:
    files = file.read().splitlines()

for fileName in files:
    dirPath = os.path.join(path, fileName)
    with open(dirPath, "w"):
        pass
