import unittest
from student import Student
from datetime import timedelta
from unittest.mock import patch


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

    # test to mock successful request
    def test_course_schedule_success(self):
        # use patch as a context manager to mock a get request
        # in the student module
        with patch("student.requests.get") as mocked_get:
            # set specific values to mock successful requests
            mocked_get.return_value.ok = True
            mocked_get.return_value.text = "Success"
            # get the student course schedule and store it in a var
            # and compare the returned response with the Success str
            schedule = self.student.course_schedule()
            self.assertEqual(schedule, "Success")

    def test_course_schedule_fail(self):
        with patch("student.requests.get") as mocked_get:
            mocked_get.return_value.ok = False

            schedule = self.student.course_schedule()
            self.assertEqual(schedule, "Something went wrong!")


if __name__ == '__main__':
    unittest.main()
