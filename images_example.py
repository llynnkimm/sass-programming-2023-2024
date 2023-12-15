# Images and Python

from PIL import Image

# Open an image and read the information from the image

# open the file
with Image.open("./Images/kid-green.jpg") as im:
    # visit every pixel in the image
    image_height = im.height
    image_width = im.width

    # left-to-right, top-to-bottom
    for y in range(image_height):
        for x in range(image_width):
            # print out the pixel information for every pixel
            pixel = im.getpixel((x, y))

            