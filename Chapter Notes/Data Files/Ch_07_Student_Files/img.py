from images import Image

def main():
    img = Image("smokey.gif")
    blue = (0, 0, 255)
    y = img.getHeight() // 2
    for x in range(img.getWidth()):
        img.setPixel(x, y - 1, blue)
        img.setPixel(x, y, blue)
        img.setPixel(x, y + 1, blue)
    img.draw()

if __name__ == "__main__":
   main()
