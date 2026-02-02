"""
File: blur.py
Name: Alan
-------------------------------
This file shows the original image first,
smiley-face.png, and then compare to its
blurred image. The blur algorithm uses the
average RGB values of a pixel's nearest neighbors.
"""

from simpleimage import SimpleImage


def blur(img):
    """
    Takes an image and returns a blurred version.
    The algorithm calculates the average RGB values of the 3x3 grid around each pixel.
    :param img: SimpleImage, the original image to be processed.
    :return: SimpleImage, after blurred effect image
    """
    new_img = SimpleImage.blank(img.width, img.height)
    for y in range(img.height):
        for x in range(img.width):
            # Reset counters for the new pixel
            total_r = 0
            total_g = 0
            total_b = 0
            count = 0
            for i in range(x-1, x+2):  # Loop over neighboring pixels
                for j in range(y-1, y+2):
                    if 0 <= i < img.width and 0 <= j < img.height:  # Position can't exceed canvas range
                        imgp = img.get_pixel(i, j)
                        total_r += imgp.red
                        total_g += imgp.green
                        total_b += imgp.blue
                        count += 1  # Increment valid neighbor count
            new_imgp = new_img.get_pixel(x, y)
            new_imgp.red = total_r // count
            new_imgp.green = total_g // count
            new_imgp.blue = total_b // count
    return new_img


def main():
    """
    Blur the image and show the comparison between the original and the blurred result.
    """
    old_img = SimpleImage("images/smiley-face.png")
    old_img.show()

    blurred_img = blur(old_img)
    for i in range(10):
        blurred_img = blur(blurred_img)
    blurred_img.show()


# ---- DO NOT EDIT CODE BELOW THIS LINE ---- #

if __name__ == '__main__':
    main()
