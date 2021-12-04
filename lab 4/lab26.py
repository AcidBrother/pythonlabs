'''
#26.1
from PIL import Image

def gradient(color):
    color = color.upper()
    im = Image.new("RGB", (512, 200), (0, 0, 0))
    pixels = im.load()
    r = 0
    g = 0
    b = 0
    if color == 'R':
        for i in range(512):
            if i % 2 == 0 and i != 0:
                r += 1
            for j in range(200):
                pixels[i, j] = r, g, b

    elif color == 'G':
        for i in range(512):
            if i % 2 == 0 and i != 0:
                g += 1
            for j in range(200):
                pixels[i, j] = r, g, b

    elif color == 'B':
        for i in range(512):
            if i % 2 == 0 and i != 0:
                b += 1
            for j in range(200):
                pixels[i, j] = r, g, b
    im.save("res.png", "PNG")


gradient("R")
'''


'''
#26.2
from PIL import Image
from PIL import ImageDraw


def board(num, size):
    new_color = (255, 255, 255)
    new_image = Image.new("RGB", (num * size, num * size), new_color)
    x = size * num
    y = x
    draw = ImageDraw.Draw(new_image)
    for i in range(0, x, size):
        if i % (size * 2) == 0:
            for j in range(0, y, size):
                if j % (size * 2) == 0:
                    draw.rectangle(
                        [i, j, i + size - 1, j + size - 1], fill='black')
        else:
            for j in range(size, y, size):
                if j % (size * 2) != 0:
                    draw.rectangle(
                        [i, j, i + size - 1, j + size - 1], fill='black')
    new_image.save('result.png', "PNG")

board(16,16)
'''

'''
#26.3
from PIL import Image


def makeanagliph(filename, delta):
    im = Image.open(filename)
    x, y = im.size
    res = Image.new('RGB', (x, y), (0, 0, 0))
    pixels2 = res.load()
    pixels = im.load()
    for i in range(x):
        for j in range(y):
            if i < delta:
                r, g, b = pixels[i, j]
                pixels2[i, j] = 0, g, b
            else:
                g, b = pixels[i, j][1:]
                r = pixels[i - delta, j][0]
                pixels2[i, j] = r, g, b
    res.save("ress.jpg")


if __name__ == "__main__":
    makeanagliph("pic.jpg", 10)
'''

'''
#26.4
from PIL import Image, ImageDraw

im = Image.open("lena.pgm")

draw = ImageDraw.Draw(im)
draw.line((0, 0) + im.size, fill=128)
draw.line((0, im.size[1], im.size[0], 0), fill=128)
del draw

# write to stdout
im.save(sys.stdout, "PNG")
'''
