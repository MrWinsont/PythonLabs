from sys import argv
from pathlib import Path

from PIL import Image
import matplotlib.pyplot as plt


def main():
    if len(argv) == 2:
        path = Path(argv[1])
    else:
        print("enter a path to your jpg file")

    img = Image.open(path)

    fig = plt.figure(figsize=(15,11))
    grid = fig.add_gridspec(4,2)

    gridImage = fig.add_subplot(grid[0,0])
    gridImage.imshow(img)
    gridImage.set_title("Original Image")

    r, g, b = img.split()
    grayImage = img.convert('L')
    imgHisogram = grayImage.histogram()

    imageHistogram = fig.add_subplot(grid[0,1])
    imageHistogram.plot(range(256), imgHisogram, color = 'gray')
    imageHistogram.set_title("Image Histogram")

    colors = ['red', 'green', 'blue']
    row = 1
    for item in [r, g, b]:
        colorHist = fig.add_subplot(grid[row,1])
        colorHist.plot(range(256), item.histogram(), color = colors[row-1])
        colorHist.set_title(f'{colors[row-1]} channel histogramm')
        row+=1

    plt.tight_layout()
    plt.show()

main()