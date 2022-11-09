import random
import string

def get_flag():
    return f"flag{'{'+ ''.join(random.choices(string.ascii_letters + string.digits, k=8)) + '}'}"