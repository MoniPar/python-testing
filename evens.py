"""
Should raise a TypeError if a list is not passed into the function.
error message: "A list was not passed into the function"
If numbers is empty return False
If the number of even numbers is odd, return False
If the number of even numbers is 0, return False
If the number of even numbers is even, return True
"""


def even_number_of_evens(numbers):
    if isinstance(numbers, list):
        if numbers == []:
            return False
        else:
            evens = 0

        for n in numbers:
            # check if the number is even
            if n % 2 == 0:
                # if it is increment the evens variable
                evens += 1

        # if there are even numbers
        if evens:
            # check if the evens variable is an even number
            # this will return True if the n of evens is even
            return evens % 2 == 0
        else:
            return False

    else:
        raise TypeError("A list was not passed into the function")


if __name__ == '__main__':
    print(even_number_of_evens([5]))
