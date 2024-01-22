# Lynn Kim
# December 13

# Do you need help with colours?
# This is for you!

def pixel_to_string(pixel: tuple) -> str:
    """Take a rgb 3-tuple and "interpret it"
    as a colour and return that colour's name

    Params:
        pixel - 3-tuple of (red, green, blue)

    Return:
        String representing the colour
    """
    r, g, b = pixel

    if g > 140 and r < 32 and b < 45:
        return "green"
    
def is_light(pixel:tuple) -> bool:
    """ Take a pixel
    """
    red = pixel[0]
    green = pixel[1]
    blue = pixel[2]

    # calculate the average value of all three (red, green, blue)
    average = (red + green + blue) / 3

    # if the average >= 128 return True
    if average >= 128:
        return True
    
    # else return false
    else:
        return False
    
black_pixel = (0, 0, 0)
dark_gray_pixel = (127, 127, 127)
light_gray_pixel = (128 ,128, 128)
white_pixel = (255, 255, 255)
print(is_light(black_pixel)) # False
print(is_light(dark_gray_pixel)) # False
print(is_light(light_gray_pixel)) # True
print(is_light(white_pixel)) # True