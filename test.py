import unittest
from functions import *



class ValidateDateTestCase(unittest.TestCase):
    def test_valid_date(self):
        date_string = "2022-06-10"
        expected_output = True
        actual_output = validate_date(date_string)
        self.assertEqual(actual_output, expected_output)

    def test_invalid_format(self):
        date_string = "June 10, 2022"
        expected_output = False
        actual_output = validate_date(date_string)
        self.assertEqual(actual_output, expected_output)

    def test_invalid_date(self):
        date_string = "2022-06-31"
        expected_output = False
        actual_output = validate_date(date_string)
        self.assertEqual(actual_output, expected_output)



# class ValidateEmailTestCase(unittest.TestCase):
#     def test_valid_email(self):
#         valid_emails = [
#             "test@example.com",
#             "test.email@example.com",
#             "test_email@example.com",
#             "test.email+label@example.com",
#             "1234@test.example.com",
#             "test@example.co.uk",
#             "test@example.org"
#         ]
#         for email in valid_emails:
#             with self.subTest(email=email):
#                 self.assertTrue(validate_email(email))

#     def test_invalid_email(self):
#         invalid_emails = [
#             "test@example",
#             "test.example.com",
#             "test@example..com",
#             "@example.com",
#             "test@.example.com",
#             "test@example..com",
#             "test@example.",
#             "test@example.com.",
#             "test@.com",
#             "test@",
#             "test"
#         ]
#         for email in invalid_emails:
#             with self.subTest(email=email):
#                 self.assertFalse(validate_email(email))
                
                
                
# class ValidNumberTestCase(unittest.TestCase):

#     def test_valid_egyptian_number(self):
#         # Test a valid Egyptian mobile number
#         result = validNumber("01234567890")
#         self.assertTrue(result)

#     def test_invalid_egyptian_number(self):
#         # Test an invalid Egyptian mobile number
#         result = validNumber("01234567890")
#         self.assertFalse(result)

#     def test_non_numeric_input(self):
#         # Test input that contains non-numeric characters
#         result = validNumber("0 123 456 7890")
#         self.assertTrue(result)

#     def test_short_input(self):
#         # Test input that is too short
#         result = validNumber("012345678")
#         self.assertFalse(result)

#     def test_long_input(self):
#         # Test input that is too long
#         result = validNumber("012345678901")
#         self.assertFalse(result)

 
class TestRegister(unittest.TestCase):
    def test_register(self):
        # Test registration of a new user
        user_count = len(user.users)
        # Mock user input
        mock_input = ["Test", "User", "testuser@gmail.com", "password123", "01234567890"]
        original_input = __builtins__.input
        __builtins__.input = lambda _: mock_input.pop(0)
        # Call register function
        register()
        # Restore input function
        __builtins__.input = original_input
        # Assert that user was added to users list
        self.assertEqual(len(user.users), user_count + 1)
        
if __name__ == "__main__":
    unittest.main()