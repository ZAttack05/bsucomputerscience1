from functools import reduce

def blur(image, offset):
    """Builds and returns a new image which is
ablurred copy of the argument image."""
    def tripleSum(triple1, triple2):
        (r1, g1, b1) = triple1
        (r2, g2, b2) = triple2
        return (r1 + r2, g1 + g2, b1 + b2)

    new = image.clone()
    
    for y in range(offset, image.getHeight() - offset):
        for x in range(offset, image.getWidth() - offset):

            l=[]
            for i in range(-offset, offset+1):
                for j in range(-offset, offset+1):
                    l.append(image.getPixel(x+i, y+j))
          
            sums = reduce(tripleSum,l)
            averages = tuple(map(lambda x: x // len(l), sums))
            new.setPixel(x, y, averages)
    return new
