import random
import string


def password_generator():
    length = random.randint(14, 24)
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    num = string.digits
    symbols = string.punctuation

    all_parts = lower + upper + num + symbols

    temp = random.sample(all_parts, length)
    password = "".join(temp)
    return password


print(password_generator())
