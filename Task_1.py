import sys
import re
import string


def check_password_1(pwd):
    return pwd


def check_password(pwd):
    str_punc = string.punctuation
    conds = {
        "- The password must contain both lowercase and uppercase characters":
            lambda s: re.search(r"[A-Z]+", s) and re.search(r"[a-z]+", s),
        "- The password must contain at least one digit": lambda s: re.search(r"[\d]+", s),
        '''- The password must contain at least one punctuation character (!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~) ''':
            lambda s: re.search(rf"[{str_punc}]+", s),
        "- The password must be at least 14 characters long": lambda s: len(s) >= 14
    }

    # lambda s: re.search(rf"[{string.punctuation}]", s),
    valid = True
    for name, cond in conds.items():
        if not cond(pwd):
            valid = False
    if valid:
        print("Strong password")
    else:
        print("Password Weak:")
        for name, cond in conds.items():
            if not cond(pwd):
                print(name)

    return valid


# try:
#     user_password = sys.argv[1]
#     check_password(user_password)
# except IndexError:
#     print('Unable to read your password as a command line argument')
#
#









