from PIL import Image, ImageFilter, ImageFont, ImageDraw
import random

im = Image.open('Asset/WechatIMG78.jpeg')
w, h = im.size
print('original image size: %sx%s' % (w, h))

# 缩略图
im.thumbnail((w // 2, h // 2))
im.save('Asset/thumbnail.jpeg', 'jpeg')
print('thumbnail image size: %sx%s' % im.size)

# 模糊
im2 = im.filter(ImageFilter.BLUR)
im2.save('Asset/blur.jpeg', 'jpeg')

def randomChar():
    return chr(random.randint(65, 90))

def randomColor():
    return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

width = 60 * 4
height = 60
codeImage = Image.new('RGB', (width, height), (255, 255, 255))
font = ImageFont.truetype('Arial.ttf', 36)

draw = ImageDraw.Draw(codeImage)

for x in range(width):
    for y in range(height):
        draw.point((x, y), fill=randomColor())

for t in range(4):
    draw.text((60 * t + 10, 10), randomChar(), font = font, fill = randomColor())

codeImage = codeImage.filter(ImageFilter.BLUR)
codeImage.save('Asset/codeImage.jpeg', 'jpeg')
