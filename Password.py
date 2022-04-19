import re
import string
import random


class Password(object):
    @staticmethod
    def validate(pwd: str) -> bool:
        conds = {
            "- The password must contain both lowercase and uppercase characters":
                lambda s: re.search(r"[A-Z]+", s) and re.search(r"[a-z]+", s),
            "- The password must contain at least one digit": lambda s: re.search(r"[\d]+", s),
            '''- The password must contain at least one punctuation character (!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~)''':
                lambda s: re.search(rf"[{string.punctuation}]+", s),
            "- The password must be at least 14 characters long": lambda s: len(s) >= 14
        }

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

    @staticmethod
    def generate(length: int) -> str:
        lower = string.ascii_lowercase
        upper = string.ascii_uppercase
        num = string.digits
        symbols = string.punctuation

        all_parts = lower + upper + num + symbols

        temp = random.sample(all_parts, length)
        password = "".join(temp)

        return password

