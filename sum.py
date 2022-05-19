
from unittest import result


def my_function(num1, num2):
    return num1 + num2


if __name__ == "__main__":
    number1 = int(input("Enter a first number: "))
    number2 = int(input("Enter a second number: "))

    print(my_function(number1, number2))
