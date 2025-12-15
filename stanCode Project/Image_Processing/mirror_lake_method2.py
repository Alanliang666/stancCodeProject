"""
File: mirror_lake.py
Name: Alan
----------------------------------
This program reads the image “mt-rainier.jpg” and generates a 
new image that creates a mirror-lake effect by placing an 
inverted copy of the original image beneath it.
"""


from simpleimage import SimpleImage


def reflect(filename):
    """
    :param filename: str, The filepath that stores the image to be processed.
    :return: SimpleImage, The resulting image with a mirror-lake effect.
    """
    img = SimpleImage(filename)
    b_img = SimpleImage.blank(img.width, img.height*2)
    for y in range(img.height):
        for x in range(img.width):
            imgp = img.get_pixel(x, y)
            b_img.set_rgb(x, y, imgp.red, imgp.green, imgp.blue)
            b_img.set_rgb(x, b_img.height-1-y, imgp.red, imgp.green, imgp.blue)
    return b_img


def main():
    """
    Reads the original image and displays both the original and the mirrored version.
    """
    original_mt = SimpleImage('images/mt-rainier.jpg')
    original_mt.show()
    reflected = reflect('images/mt-rainier.jpg')
    reflected.show()


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    main()
