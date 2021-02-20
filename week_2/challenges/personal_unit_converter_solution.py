# THIS IS A SAMPLE SOLUTION
import math


def grading(score) -> str:
    """
    Converts percentage into letter grade.
    """
    if score < 50:
        grade = "F"
    elif score >= 50 and score < 60:
        grade = "D"
    elif score >= 60 and score < 70:
        grade = "C"
    elif score >= 70 and score < 80:
        grade = "B"
    elif score >= 80 and score <= 100:
        grade = "A"
    else:
        print("Please a positive number that is less than or equal to 100.")
        grade = "Unknown"
    return grade


def convert_weight_pounds(weight) -> int:
    """
    Converts Kilograms into Pounds
    """
    pounds = round((weight * 2.20462), 5)
    return pounds


def convert_to_binary(decimal) -> str:
    """
    Converts Decimal numbers into Binanry Digits
    """
    binary = bin(decimal).replace("0b", "")
    return binary


def inches_to_pixels(inches):
    """
    Converts Inches into Pixels
    """
    pixels = inches / 0.0104166666667
    return round(pixels, 0)


def minutes_to_hours(minutes):
    """
    Converts Minutes into Hours and Minutes
    """
    hours = math.trunc(minutes / 60)
    mins = minutes % 60
    return f"{hours} Hours and {mins} Mins"


if __name__ == "__main__":
    name = input("Please enter your name: ")
    print(f"\nHello {name.capitalize()}, welcome to your personal unit converter.")
    print(
        """
    Please choose the conversion you would like to perform:
        1 - Convert Percentages to Letter Grades
        2 - Convert Kilograms to Pounds
        3 - Convert Decimal to Binary
        4 - Convert Inches to Pixels
        5 - Convert Minutes to Hours ans Minutes
        """
    )
    # Cobmining While loop and error catching ensures user enters required datatype (only integer)
    while True:
        try:
            choice = int(input("Choice: "))
            if choice == 1:
                while True:
                    try:
                        score = int(input("Percent to convert to letter grade: "))
                        converted = grading(score)
                        print(f"{score}% = {converted}")
                        break
                    except ValueError:
                        pass
            elif choice == 2:
                while True:
                    try:
                        weight = int(input("Value in Kilograms to convert: "))
                        converted = convert_weight_pounds(weight)
                        print(f"{weight} Kgs = {converted} Pounds")
                        break
                    except ValueError:
                        pass
            elif choice == 3:
                while True:
                    try:
                        decimal = int(input("Value in Decimal to convert: "))
                        converted = convert_to_binary(decimal)
                        print(f"{decimal} = {converted}")
                        break
                    except ValueError:
                        pass
            elif choice == 4:
                while True:
                    try:
                        inches = float(input("Value in Inches to convert: "))
                        converted = inches_to_pixels(inches)
                        print(f"{inches} Inches = {converted} Pixels")
                        break
                    except ValueError:
                        pass
            elif choice == 5:
                while True:
                    try:
                        minutes = int(input("Value in Minutes to convert: "))
                        converted = minutes_to_hours(minutes)
                        print(f"{minutes} Minutes = {converted}")
                        break
                    except ValueError:
                        pass
            break
        except ValueError:
            pass
    print(f"\nGoodbye {name.capitalize()}")