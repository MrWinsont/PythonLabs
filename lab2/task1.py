from PIL import Image
from argparse import ArgumentParser


with Image.open("images/image1.jpg") as img:
    r, g, b = img.split()

    newWidth = img.width * 4
    output = Image.new('RGB', (newWidth, img.width))

    output.paste(img)
    output.paste(r.convert('RGB'), (img.width, 0))
    output.paste(g.convert('RGB'), (img.width * 2, 0))
    output.paste(b.convert('RGB'), (img.width * 3, 0))

    output.show()
    output.save("images/output1.jpg", "jpeg")