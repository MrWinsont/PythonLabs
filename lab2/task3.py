from PIL import Image, ImageDraw, ImageFont

def watermark(srcImagePath, srcWatermarkImagePath, dirImagePath, watermatkText, posImage, posText):
    with Image.open(srcImagePath) as img, Image.open(srcWatermarkImagePath) as newimg:
        output = ImageDraw.Draw(img)

        newimg = newimg.resize((200, 200))

        img.paste(newimg, posImage)
        drawing = ImageDraw.Draw(img)
        font = ImageFont.load_default(size=30)
        drawing.text(posText, watermatkText, fill=(0, 0, 255), font=font)

        img.show()
        img.save(dirImagePath, "jpeg")
if __name__ == '__main__':
    srcImage = "images/image3.jpg"
    srcWatermark = "images/wmimg3.jpg"
    dirPath = "images/task3.jpg"
    watermark(srcImage, srcWatermark, dirPath, watermatkText='Grin Vitaly', posImage=(10, 10), posText=(10, 10))




