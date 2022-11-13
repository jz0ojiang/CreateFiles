import random
from faker import Faker
import os

from utils.utils import get_flag
from utils.flags import flags

fake = Faker()

def generate_text_file(path):
    if not os.path.exists(path):
        os.makedirs(path)
    filename = fake.name().replace(" ", "_") + f"_{random.randint(1000,9999)}" + ".txt"
    flag = get_flag()
    with open(os.path.join(path, filename), "w") as f:
        f.write(flag + "\n" + fake.text())
    return os.path.join(path, filename),flag

def generate_text_files(path, count):
    for _ in range(count):
        flags.add(generate_text_file(path))