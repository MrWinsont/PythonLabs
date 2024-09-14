from PIL import Image, ImageDraw, ImageFont

for i in range(1, 4):
    width, height = 100, 100
    img = Image.new('RGB', (width, height), 'white')
    draw = ImageDraw.Draw(img)

    draw.line([(0, 0), (100, 0), (100, 100), (0, 100), (0, 0)], width=5, fill=(0, 0, 255))

    font = ImageFont.load_default(40)

    textPos = (width // 2, height // 2)

    draw.text(textPos, str(i), anchor="mm", font=font, fill='red')
    img.show()
    img.save(f"images/{i}.png", format="png")