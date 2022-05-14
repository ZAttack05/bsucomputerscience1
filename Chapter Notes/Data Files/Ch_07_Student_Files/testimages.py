from images import Image
from blur import *

def main():
    img = Image("smokey.gif")
    img.draw()
    new_img = blur(img)
    new_img.draw()

if __name__ == "__main__":
   main()
