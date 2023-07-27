import unittest
from evens import even_number_of_evens


class TestEvens(unittest.TestCase):

    def test_throws_error_if_value_passed_in_is_not_list(self):
        # assertion checks if a TypeError is raised when a function is called
        # with the value of 4 - (func set to return None)
        self.assertRaises(TypeError, even_number_of_evens, 4)

    def test_values_in_list(self):
        # assertion checks if empty list has been passed in
        # should expect False
        self.assertEqual(even_number_of_evens([]), False)
        # assertion checks if even numbers are passed in
        # should expect True
        self.assertEqual(even_number_of_evens([2, 4]), True)
        # assertion checks if there is one even number passed in
        # should expect False
        self.assertEqual(even_number_of_evens([2]), False)
        # assertion checks if there is an odd number of odd numbers passed in
        # should expect False
        self.assertEqual(even_number_of_evens([1, 3, 5]), False)


if __name__ == '__main__':
    unittest.main()
