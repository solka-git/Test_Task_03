import sys
from Password import Password


if __name__ == "__main__":
    try:
        user_password = sys.argv[1]
        Password.validate(user_password)
    except IndexError:
        print('Unable to read your password as a command line argument')
