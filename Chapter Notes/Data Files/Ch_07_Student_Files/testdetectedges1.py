"""
File: testdetectedges.py
Tests a function for detecting edges in an image.
"""

from images import Image
from blurStrong import *

def detectEdges(image, amount):
    """Builds and returns a new image in which the 
    edges of the argument image are highlighted and
    the colors are reduced to black and white."""

    def average(triple):
        (r, g, b) = triple
        return (r + g + b) / 3

    blackPixel = (0, 0, 0)
    whitePixel = (255, 255, 255)
    new = image.clone()
    for y in range(image.getHeight() - 1):
        for x in range(1, image.getWidth()):
            oldPixel = image.getPixel(x, y)
            leftPixel = image.getPixel(x - 1, y)
            bottomPixel = image.getPixel(x, y + 1)
            oldLum = average(oldPixel)
            leftLum = average(leftPixel)
            bottomLum = average(bottomPixel)
            if abs(oldLum - leftLum) > amount or \
               abs(oldLum - bottomLum) > amount:
                new.setPixel(x, y, blackPixel)
            else:
                new.setPixel(x, y, whitePixel)
    return new

def main(filename = "smokey.gif"):
    image = Image(filename)
    print("Close the image window to continue. ")
    image.draw()
    image1 = blur(image,3) # offset of 3 means 7x7 neighbourhood
    image1.draw()
    image2 = detectEdges(image1, 5)
    print("Close the image window to continue. ")
    image2.draw()
    image3 = detectEdges(image1, 10)
    print("Close the image window to continue. ")
    image3.draw()
    print("Close the image window to quit. ")

if __name__ == "__main__":
   main()

