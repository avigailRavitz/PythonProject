
import os
import re



def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


if __name__ == '__main__':
    print_hi('PyCharm')



def check_file_existence(file_path):
    if not os.path.exists(file_path):
        # Create the file and the directory if they do not exist
        directory = os.path.dirname(file_path)
        os.makedirs(directory, exist_ok=True)
        with open(file_path, 'w') as new_file:
            new_file.write("This is a new file.")
        print(f"File {file_path} did not exist and was created.")
    else:
        print(f"File {file_path} already exists.")


def read_user_file(file_path):
    with open(file_path, 'r') as user_file:
        for line in user_file:
            yield line.strip()


class SmartArray:
    def __init__(self, data):
        self.data = data


def get_subset(self):
    ten_percent = int(0.1 * len(self.data))
    return self.data[:ten_percent]


def process_even_rows(users):
    for i, user in enumerate(users, start=1):
        if i % 2 == 0:
            print(f"Processing user in even row: {user}")


def is_valid_email(email):
    email_pattern = re.compile(r"[^@]+@[^@]+\.[^@]+")
    return bool(email_pattern.match(email))


def read_email_file(file_path):
    with open(file_path, 'r') as email_file:
        return [line.strip() for line in email_file]


def validate_emails(emails):
    for email in emails:
        if is_valid_email(email):
            print(f"{email} is a valid email address.")
        else:
            print(f"{email} is not a valid email address.")


def get_gmail_addresses(emails):
    gmail_addresses = [email for email in emails if email.endswith('@gmail.com')]
    return gmail_addresses


def check_email_username_match(emails, usernames):
    result = []
    for email, username in zip(emails, usernames):
        if username.lower() in email.lower():
            result.append(True)
        else:
            result.append(False)
    return result


def count_letter_a_in_name(user_name):
    ascii_values = [ord(char) for char in user_name]
    count_a = ascii_values.count(ord('A'))
    return count_a


def validate_and_capitalize_usernames(usernames):
    valid_usernames = [name.capitalize() for name in usernames if name.isalpha()]
    return valid_usernames


def calculate_payment_for_team(customers):
    total_payment = 0
    for i, customer in enumerate(customers, start=1):
        if i % 8 == 0:
            total_payment += 200
        elif i > 8 and i % 8 == 1:
            total_payment += 50
    return total_payment

"""


# 1.
check_file_existence("Data/UsersName.txt")

# 2.
user_generator = read_user_file("Data/UsersName.txt")
user_array = SmartArray(list(user_generator))
subset_of_users = user_array.get_subset()
print("Subset of users:", subset_of_users)

# 4.
emails = read_email_file("Data/UsersEmail.txt")
validate_emails(emails)

# 5.
gmail_addresses = get_gmail_addresses(emails)
print("Gmail addresses:", gmail_addresses)

# 6
"""
emails = read_email_file("Data/UsersEmail.txt")
usernames = ["user1", "user2", "user3", "user4"]
matches = check_email_username_match(emails, usernames)
print("Email matches username:", matches)
"""
# 7.
user_name = "bela"
count_a = count_letter_a_in_name(user_name)
print("Number of 'A' in the user name:", count_a)

# 8.
usernames = ["lea", "so", "mike123", "riki"]
validated_usernames = validate_and_capitalize_usernames(usernames)
print("Validated and capitalized usernames:", validated_usernames)

# 9.
customers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]
total_payment = calculate_payment_for_team(customers)
print("Total payment for the team:", total_payment)


"""
