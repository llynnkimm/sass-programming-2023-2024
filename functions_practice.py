# Lynn Kim
# NOvember 24

def area_of_a_square(sidelength: float) -> float:
    """Return the area of a square.
    Results are in units squared.

    Params:
    sidelength - length of one side of the square
    """

    area = sidelength**2
    return area

def print_area_of_a_square(sidelength: float) -> None:
    """Calculate and print the area of a square.
    Results are in units squared.

    Params:
    sidelength - length of one side of the square
    """

    area = sidelength**2

    print(
        f"The area of a square with side length {sidelength} is: {area} square units."
    )

print(print_area_of_a_square(12.2))
# print_area_of_a_square(12)

# Given two squares of two sidelengths
#    12.2 and 144
# Add the area of both squares
# area_of_squares = area_of_a_square(12.2) + area_of_a_square(144)
# print(area_of_squares)

# stars()
def stars(num_of_stars: int) -> str:
    """Return the area of stars.

    Params:
    num_stars - The numbers of stars to return
    """

    return "*" * num_of_stars

print(stars(100))

# biggest_of_three
def biggest_of_three(sidelength: float) -> float:
    """Return the area of a square.
    Results are in units squared.

    Params:
    sidelength - length of one side of the square
    """

    area = sidelength**2
    return area