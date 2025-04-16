from static.handlers import get_valid_input
from static.validator import validate_username, validate_password
import sys

class Authenticator:
    def __init__(self):
        self.username = None
        self.password = None

    def authenticate_user(self):
        self.username = get_valid_input(
            "Enter your username (4-10 characters, alphanumeric): ",
            validate_username,
            allow_cancel=False
        )
        if self.username is None:
            print("Invalid username, Exiting application...")
            sys.exit()
        self.password = get_valid_input(
            "Set your password (4-10 characters, must include letters and numbers): ",
            validate_password,
            allow_cancel=False
        )
        if self.username is None:
            print("Invalid password, Exiting application...")
            sys.exit()
        return self.username, self.password