import random
from Password import Password


if __name__ == "__main__":
    print(Password.generate(random.randint(14, 80)))
