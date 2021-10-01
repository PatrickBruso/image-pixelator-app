"""
This program takes a user-chosen image and returns that image and a new image
that is a pixelated version of the original image set to a user-chosen palette
of colors.

Version 2.0 is an implementation in Tkinter to allow for palette choice.
"""

from simpleimage import SimpleImage
import math


def main(file_location):  # change to filename and take in the filename and then open as image
    """
    Receive user inputs for images and palette and then call functions to obtain
    pixelated copy of image.
    :return: original image and pixelated copy of image
    """
    # create lists for the images and the palettes
    image_list = ['dog.png', 'landscape.jpg', 'landscape.png']
    palette_list = ['cybear9.png', 'endesga32.png', 'ammo8.png', 'dreamscape8.png', 'funkyfuture8.png',
                    'pollen8.png', 'retrocal8.png']

    image = SimpleImage(file_location)

    print("\nList of palettes: ")
    for palettes in palette_list:
        print(palette_list.index(palettes) + 1, palettes)

    palette_name = input("\nGive me a palette choice: ")
    while True:
        try:
            palette = SimpleImage(f'Palettes/{palette_name}')
            break
        except FileNotFoundError:
            filename = input("Not found. Try again: ")

    image_copy = shrink(image)

    # image.show()

    new_image = pixelate(image_copy, palette)
    pixel_image = expand(new_image)

    return new_image  # or save new file and then send through the address?


def shrink(image):
    """
    Function that takes an image and returns a copy of that image that is reduced by 4 times.
    Each 4x4 grid of pixels in the original image will be 1 pixel in the new image.
    :param image: image that user wants to shrink
    :return: shrunken image as a copy
    """
    image_copy = SimpleImage.blank(image.width // 4, image.height // 4)  # create bank image that is 4 times smaller

    # set original coordinates and coordinates for image copy
    y = 0
    x = 0
    x_coord = 0
    y_coord = 0

    # while loop to work through the x indices and y indices of original picture
    while y < image.height - 2:
        while x < image.width - 2:
            # copy image is created using the average of the 4x4 pixel grid
            image_copy.set_pixel(x_coord, y_coord, get_grid_average(x, y, image))
            x_coord += 1
            x += 4
        x = 0
        x_coord = 0
        y_coord += 1
        y += 4

    return image_copy


def get_grid_average(x, y, image):
    """
    Function that takes in an x and y coordinate for a pixel on an image and
    returns the average of the colors of a range that is 4x4 grid starting at that coordinate.
    :param x: x coordinate in image
    :param y: y coordinate in image
    :param image: image to obtain colors from
    :return: average pixel color over 2x2 grid area
    """
    # initialize empty lists for RGB values
    red = []
    green = []
    blue = []

    counter = 0

    # for each 4x4 grid get the pixel and then add the RGB values to list
    for i in range(x, x + 4):
        for j in range(y, y + 4):
            pixel = image.get_pixel(i, j)
            red.append(pixel.red)
            green.append(pixel.green)
            blue.append(pixel.blue)
            counter += 1

    # get average of each RGB value and return that average as a pixel
    pixel.red = sum(red) // counter
    pixel.green = sum(green) // counter
    pixel.blue = sum(blue) // counter

    return pixel


def expand(image):
    """
    Function that takes an image and returns a copy that is 4 times larger.
    Each pixel of the original image is set to a 4x4 grid of pixels in the copy image.
    :param image: image to enlarge
    :return: enlarged image as a copy
    """
    # create blank canvas that is 4 times larger than original
    expanded_image = SimpleImage.blank(image.width * 4, image.height * 4)

    # set initial coordinates for target image and copy image
    y = 0
    x = 0
    x_coord = 0
    y_coord = 0

    # while loop to draw a 4x4 grid of pixels for each pixel in original image keeping the same RGB values
    while y < image.height:
        while x < image.width:
            expanded_image.set_pixel(x_coord, y_coord, image.get_pixel(x, y))
            expanded_image.set_pixel(x_coord + 1, y_coord, image.get_pixel(x, y))
            expanded_image.set_pixel(x_coord + 2, y_coord, image.get_pixel(x, y))
            expanded_image.set_pixel(x_coord + 3, y_coord, image.get_pixel(x, y))
            expanded_image.set_pixel(x_coord, y_coord + 1, image.get_pixel(x, y))
            expanded_image.set_pixel(x_coord, y_coord + 2, image.get_pixel(x, y))
            expanded_image.set_pixel(x_coord, y_coord + 3, image.get_pixel(x, y))
            expanded_image.set_pixel(x_coord + 2, y_coord + 1, image.get_pixel(x, y))
            expanded_image.set_pixel(x_coord + 3, y_coord + 1, image.get_pixel(x, y))
            expanded_image.set_pixel(x_coord + 3, y_coord + 2, image.get_pixel(x, y))
            expanded_image.set_pixel(x_coord + 1, y_coord + 2, image.get_pixel(x, y))
            expanded_image.set_pixel(x_coord + 1, y_coord + 3, image.get_pixel(x, y))
            expanded_image.set_pixel(x_coord + 2, y_coord + 3, image.get_pixel(x, y))
            expanded_image.set_pixel(x_coord + 1, y_coord + 1, image.get_pixel(x, y))
            expanded_image.set_pixel(x_coord + 2, y_coord + 2, image.get_pixel(x, y))
            expanded_image.set_pixel(x_coord + 3, y_coord + 3, image.get_pixel(x, y))
            x_coord += 4
            x += 1
        x = 0
        x_coord = 0
        y_coord += 4
        y += 1

    return expanded_image


def pixelate(image, palette):
    """
    Function that replaces pixel from target image with pixel from a set color palette
    and returns a copy of the image.
    :param image: original image
    :param palette: color palette to use
    :return: copy of image with color palette applied
    """
    image_copy = SimpleImage.blank(image.width, image.height)

    for new_pixel in image_copy:
        x = new_pixel.x
        y = new_pixel.y
        old_pixel = image.get_pixel(x, y)
        palette_color = color_picker(old_pixel, palette)  # call function to determine which color to use from palette
        new_pixel.red = palette_color[0]
        new_pixel.green = palette_color[1]
        new_pixel.blue = palette_color[2]
        image_copy.set_pixel(x, y, new_pixel)

    return image_copy


def color_picker(pixel, palette):
    """
    Function that takes in pixel from image and returns the pixel color from a palette
    which is the closest color.
    :param palette: User palette choice
    :param pixel: RGB value of pixel
    :return: closest RGB value from palette
    """
    palette_list = []

    # obtain all the RGB values for colors in a palette
    for color in palette:
        rgb_list = [color.red, color.green, color.blue]
        palette_list.append(rgb_list)

    distance_list = []

    # for each color in a palette, determine which is closest to original image color
    for color in palette_list:
        distance = int(math.sqrt((pixel.red - color[0]) ** 2 + (pixel.green - color[1]) ** 2 +
                                 (pixel.blue - color[2]) ** 2))
        distance_list.append(distance)

    closest_color = min(distance_list)
    location = distance_list.index(closest_color)

    return palette_list[location]


if __name__ == '__main__':
    main()
