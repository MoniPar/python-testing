import unittest
from student import Student
from datetime import timedelta


class TestStudent(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("set up class")

    def setUp(self):
        print("setup")
        self.student = Student("John", "Doe")

    @classmethod
    def tearDownClass(cls):
        print("tear down class")

    def tearDown(self):
        print("tear down")

    def test_full_name(self):
        # student = Student("John", "Doe")
        print("test_full_name")
        self.assertEqual(self.student.full_name, "John Doe")

    def test_alert_santa(self):
        # student = Student("John", "Doe")
        print("test_alert_santa")
        self.student.alert_santa()
        self.assertTrue(self.student.naughty_list)

    def test_email(self):
        # student = Student("John", "Doe")
        print("test_email")
        self.assertEqual(self.student.email, "john.doe@email.com")

    def test_apply_extension(self):
        print("test_apply_extension")
        official_end_date = self.student.end_date
        self.student.apply_extension(10)
        self.assertEqual(
            self.student.end_date, official_end_date + timedelta(days=10))


if __name__ == '__main__':
    unittest.main()
