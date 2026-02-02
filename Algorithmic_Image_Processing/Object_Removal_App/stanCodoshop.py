"""
File: stanCodoshop.py
Name: Alan Liang
----------------------------------------------
This program is SC101 Assignment 3 and is adapted
from Nick Parlante's Ghost assignment.

The assignment has been redesigned and extended
by Jerry Liao to fit the learning objectives of
the stanCode SC101 course.
"""

import os
import sys
import math
from simpleimage import SimpleImage


def get_pixel_dist(pixel, red, green, blue):
    """
    Computes the Euclidean color distance between a pixel's RGB values and a target mean RGB color.

    This function measures how similar a pixel is to a reference color by treating the
    red, green, and blue channels as coordinates in a 3D color space. A smaller distance
    indicates a closer color match.

    Parameters:
        pixel (Pixel): The pixel whose RGB components (pixel.red, pixel.green, pixel.blue)
            will be compared.
        red (int): The reference mean red value.
        green (int): The reference mean green value.
        blue (int): The reference mean blue value.

    Returns:
        float: The Euclidean distance between the pixel's RGB values and the reference color.
    """
    dist = math.sqrt(((red - pixel.red) ** 2 + (green - pixel.green) ** 2 + (blue - pixel.blue) ** 2))
    return dist


def get_average(pixels):
    """
    Given a list of pixels, finds their average red, blue, and green values.

    Input:
        pixels (List[Pixel]): a list of pixels to be averaged

    Returns:
        rgb (List[int]): a list of average red, green, and blue values of the pixels
                        (returns in order: [red, green, blue])
    """
    red_total = 0
    green_total = 0
    blue_total = 0
    rgb = []

    for pixel in pixels:
        red_total += pixel.red
        green_total += pixel.green
        blue_total += pixel.blue

    red_ans = red_total // len(pixels)
    green_ans = green_total // len(pixels)
    blue_ans = blue_total // len(pixels)

    rgb.append(red_ans)
    rgb.append(green_ans)
    rgb.append(blue_ans)

    return rgb


def get_best_pixel(pixels):
    """
    Selects the pixel that is closest in color to the average color of a group of pixels.

    This function examines a list of pixels and determines which one has the smallest
    color distance to the average RGB values of all pixels in the list. It is useful
    for finding the most "representative" pixel in a set.

    Parameters:
        pixels (List[Pixel]): A list of Pixel objects to evaluate.

    Returns:
        Pixel: The pixel whose color is closest to the average color of the input list.
    """
    ans_pixel = pixels[0]
    avg_pixels = get_average(pixels)
    smallest_dist = float('inf')
    for pixel in pixels:
        dist = get_pixel_dist(pixel, avg_pixels[0], avg_pixels[1], avg_pixels[2])
        if dist < smallest_dist:
            smallest_dist = dist
            ans_pixel = pixel
    return ans_pixel


def solve(images):
    """
    Given a list of image objects, compute and display the solution image
    based on images. There will be at least 3 images and they will all
    be the same size.

    Input:
        images (List[SimpleImage]): list of images to be processed
    """
    width = images[0].width
    height = images[0].height
    result = SimpleImage.blank(width, height)

    # ----- YOUR CODE STARTS HERE ----- #
    # Write code to populate image and create the 'ghost' effect
    for y in range(result.height):
        for x in range(result.width):
            pixels = []
            for image in images:
                img_p = image.get_pixel(x, y)
                pixels.append(img_p)
            b_pixel = get_best_pixel(pixels)
            result.set_rgb(x, y, b_pixel.red, b_pixel.green, b_pixel.blue)
    # ----- YOUR CODE ENDS HERE ----- #

    print("Displaying image!")
    result.show()


def jpgs_in_dir(dir):
    """
    (provided, DO NOT MODIFY)
    Given the name of a directory, returns a list of the .jpg filenames
    within it.

    Input:
        dir (string): name of directory
    Returns:
        filenames(List[string]): names of jpg files in directory
    """
    filenames = []
    for filename in os.listdir(dir):
        if filename.endswith('.jpg'):
            filenames.append(os.path.join(dir, filename))
    return filenames


def load_images(dir):
    """
    (provided, DO NOT MODIFY)
    Given a directory name, reads all the .jpg files within it into memory and
    returns them in a list. Prints the filenames out as it goes.

    Input:
        dir (string): name of directory
    Returns:
        images (List[SimpleImages]): list of images in directory
    """
    images = []
    jpgs = jpgs_in_dir(dir)
    for filename in jpgs:
        print("Loading", filename)
        image = SimpleImage(filename)
        images.append(image)
    return images


def main():
    # (provided, DO NOT MODIFY)
    args = sys.argv[1:]
    # We just take 1 argument, the folder containing all the images.
    # The load_images() capability is provided above.
    images = load_images(args[0])
    solve(images)


if __name__ == '__main__':
    main()
