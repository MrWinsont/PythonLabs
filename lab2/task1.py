from PIL import Image
from argparse import ArgumentParser


if __name__ == "__main__":
    with Image.open("images/image1.jpg") as img:
        r, g, b = img.split()

        result_img_width = img.width * 4
        result_img = Image.new('RGB', (result_img_width, img.width))

        result_img.paste(img)
        result_img.paste(r.convert('RGB'), (img.width, 0))
        result_img.paste(g.convert('RGB'), (img.width * 2, 0))
        result_img.paste(b.convert('RGB'), (img.width * 3, 0))

        result_img.show()
        result_img.save("images/output1.jpg", "jpeg")