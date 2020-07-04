import string
import random

def random_string(string_length=4):
    chars = string.ascii_letters + string.digits
    return ''.join(random.choice(chars) for i in range(string_length))
