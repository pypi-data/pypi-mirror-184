import unittest
from . import hamailtest, MongoUser


class SesMailTest(unittest.TestCase):
    def test_send_registration(self):
        user_input = {
            "email": "nayana@hiacuity.com",
            "password": "123456",
            "first_name": "nayana",
            "last_name": "hettiatachchi"}
        user = MongoUser(**user_input)
        response = hamailtest.send_registration_confirmation(user)
        self.assertIsNotNone(response)


if __name__ == '__main__':
    unittest.main()
