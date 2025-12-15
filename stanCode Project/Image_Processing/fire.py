"""
File: fire.py
Name:
---------------------------------
This file contains a function called
highlight_fires which detects the
pixels that are recognized as fire
and highlights them for better observation.
"""


from simpleimage import SimpleImage


HURDLE_FACTOR = 1.05


def highlight_fires(filename):
    """
    :param filename: str, The filepath that stores the image to be processed.
    :return: SimpleImage, The processed image with fires highlighted
    """
    img = SimpleImage(filename)
    for pixel in img:
        avg = (pixel.red+pixel.green+pixel.blue)//3
        if pixel.red > avg * HURDLE_FACTOR:
            pixel.red = 255
            pixel.green = 0
            pixel.blue = 0
        else:
            pixel.red = avg
            pixel.green = avg
            pixel.blue = avg
    return img


def main():
    """
    Detects fire regions in the photo and highlights them
    """
    original_fire = SimpleImage('images/greenland-fire.png')
    original_fire.show()
    highlighted_fire = highlight_fires('images/greenland-fire.png')
    highlighted_fire.show()


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    main()
