import random
import string

def generate_random_string(length: int) -> str:
    random_str = ''.join(random.choice(string.ascii_letters) for i in range(length))
    return random_str 
