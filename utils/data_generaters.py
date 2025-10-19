# utils/test_data_generators.py
import random
import string

def generate_user_name(uName="Ej"):
    random_uname = ''.join(random.choices(string.ascii_letters + string.digits, k=5))
    return uName+random_uname