import unittest
from io import StringIO
from unittest.mock import patch

from Task8 import is_valid_email, process_even_rows, read_email_file, get_gmail_addresses, check_email_username_match, \
    count_letter_a_in_name, validate_and_capitalize_usernames, calculate_payment_for_team


class MyTestCase(unittest.TestCase):
    def test_something(self):
        value = True
        self.assertEqual(value, value)

    @patch('sys.stdout', new_callable=StringIO)
    def test_process_even_rows(self, mock_stdout):
        users = ['Alice', 'Bob', 'Charlie', 'Dave', 'Eve']
        process_even_rows(users)
        expected_output = "Processing user in even row: Bob\nProcessing user in even row: Dave\n"
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    def test_valid_emails(self):
        # Test valid email addresses
        self.assertTrue(is_valid_email("test@example.com"))
        self.assertTrue(is_valid_email("user123@mail.co.uk"))
        self.assertTrue(is_valid_email("user.name12345@domain.org"))

    def test_invalid_emails(self):
        # Test invalid email addresses
        self.assertFalse(is_valid_email("invalid_email.com"))
        self.assertFalse(is_valid_email("user@example"))
        self.assertFalse(is_valid_email("user@.com"))
        self.assertFalse(is_valid_email("user123"))


    def test_get_gmail_addresses(self):
        emails = [
            'user1@gmail.com',
            'user2@yahoo.com',
            'user3@gmail.com',
            'user4@hotmail.com'
        ]
        gmail_addresses = get_gmail_addresses(emails)
        expected_gmail_addresses = ['user1@gmail.com', 'user3@gmail.com']
        self.assertEqual(gmail_addresses, expected_gmail_addresses)

    def test_match(self):
        emails = ["example1@example.com", "example2@example.com", "example3@example.com"]
        usernames = ["example1", "example2", "example3"]
        expected_result = [True, True, True]
        result = check_email_username_match(emails, usernames)
        self.assertEqual(result, expected_result)

    def test_no_match(self):
        emails = ["example1@example.com", "example2@example.com", "example3@example.com"]
        usernames = ["user1", "user2", "user3"]
        expected_result = [False, False, False]
        result = check_email_username_match(emails, usernames)
        self.assertEqual(result, expected_result)

    def test_no_a(self):
        user_name = "John"
        self.assertEqual(count_letter_a_in_name(user_name), 0)

    def test_one_a(self):
        user_name = "Alice"
        self.assertEqual(count_letter_a_in_name(user_name), 1)

    def test_multiple_a(self):
        user_name = "Amanda"
        self.assertEqual(count_letter_a_in_name(user_name), 1)

    def test_empty_name(self):
        user_name = ""
        self.assertEqual(count_letter_a_in_name(user_name), 0)

    def test_all_a(self):
        user_name = "AAAA"
        self.assertEqual(count_letter_a_in_name(user_name), 4)

    def test_all_valid_names(self):
        usernames = ['alice', 'bob', 'charlie']
        x = validate_and_capitalize_usernames(usernames)
        expected_result = ['Alice', 'Bob', 'Charlie']
        self.assertEqual(x, expected_result)

    def test_mixed_names(self):
        usernames = ['alice', '123bob', 'CHARLIE', 'dave!', '']
        x = validate_and_capitalize_usernames(usernames)
        expected_result = ['Alice', 'Charlie']
        self.assertEqual(x, expected_result)

    def test_empty_list(self):
        usernames = []
        x = validate_and_capitalize_usernames(usernames)
        expected_result = []
        self.assertEqual(x, expected_result)

    def test_all_invalid_names(self):
        usernames = ['123', '456', '789']
        x = validate_and_capitalize_usernames(usernames)
        expected_result = []
        self.assertEqual(x, expected_result)

    def test_empty_list(self):
        customers = []
        x = calculate_payment_for_team(customers)
        self.assertEqual(x, 0)

    def test_less_than_8_customers(self):
        customers = [1, 2, 3, 4, 5, 6, 7]
        self.assertEqual(calculate_payment_for_team(customers), 0)


if __name__ == '__main__':
    unittest.main()
