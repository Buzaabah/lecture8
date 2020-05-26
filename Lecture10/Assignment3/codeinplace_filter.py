"""
File: codeinplace_filter.py
----------------
This program implements a rad image filter.
"""

from simpleimage import SimpleImage

DEFAULT_FILE = 'images/quad.jpg'

def main():
    image_name = input("Enter an image name: ")

    # Get file and load image
    #filename = get_file()
    #image = SimpleImage(filename)
    image = SimpleImage("images/" + image_name)


    # Show the image before the transform
    image.show()
    # Apply the filter
    for y in range(image.height):
        for x in range(image.width):
            pixel = image.get_pixel(x, y)
            code_in_place_filter(pixel)

    # Show the image after the transform
    image.show()
    
def code_in_place_filter(pixel):
    Red = pixel.red
    Blue = pixel.blue
    Green = pixel.green
    pixel.red = pixel.red * 1.5
    pixel.green = pixel.green * 0.7
    pixel.blu = pixel.blue * 1.5



def get_file():
    # Read image file path from user, or use the default file
    filename = input('Enter image file (or press enter for default): ')
    if filename == '':
        filename = DEFAULT_FILE
    return filename


if __name__ == '__main__':
    main()