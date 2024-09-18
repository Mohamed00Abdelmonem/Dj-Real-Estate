import random



def generate_code(length=8):
    return ''.join([str(random.randint(0, 9)) for _ in range(length)])