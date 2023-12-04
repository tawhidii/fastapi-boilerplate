import random
import string

def random_username(length=10):
    return ''.join(random.choice(string.ascii_lowercase) for i in range(length))

def random_email(length=10):
    return ''.join(random.choice(string.ascii_lowercase) for i in range(length)) + '@test.com' 

def random_password(length=10):
    return ''.join(random.choice(string.ascii_lowercase) for i in range(length))