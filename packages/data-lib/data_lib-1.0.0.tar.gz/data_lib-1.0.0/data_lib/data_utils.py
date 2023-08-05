__author__ = "Adam Jarzebak"
__copyright__ = "Copyright 2018, Adam Jarzebak"
__credits__ = []
__license__ = "MIT"
__maintainer__ = "Adam Jarzebak"
__email__ = "adam@jarzebak.eu"
import random
import string


def generate_random_string(size: int=16) -> str:
    """
    Generates a random string with 16 characters. Size value can be changed.
    :return: random string: str
    """
    random_string = ''.join([random.choice(string.ascii_letters + string.digits) for n in range(size)])
    return random_string


def generate_random_number(size: int=8) -> str:
    """
    Generates a random number string for given size.
    :param size:
    :return:
    """
    x = [random.randint(0, 9) for p in range(0, size)]
    return ''.join(str(a) for a in x)
