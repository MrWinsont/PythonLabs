from PIL import Image
from sys import argv

if(len(argv) > 1):
    SourcePath = argv[1]
else:
    print("enter a path to your image!")
    exit()

r, g, b = 0, 0, 0
with Image.open(SourcePath) as img:
    pixels = img.load()
    for x in range(img.width):
        for y in range(img.height):
            r += pixels[x, y][0]
            g += pixels[x, y][1]
            b += pixels[x, y][2]
maxNum = "R" if r > g else "G"
maxNum = "G" if g > b else "B"
print(maxNum, "-", max(r, g, b))