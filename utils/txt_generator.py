from faker import Faker
import os

from utils.utils import get_flag

fake = Faker()

def generate_text_file(path):
    if not os.path.exists(path):
        os.makedirs(path)
    filename = fake.name().replace(" ", "_") + ".txt"
    with open(os.path.join(path, filename), "w") as f:
        f.write(get_flag() + "\n" + fake.text())
    return os.path.join(path, filename)

def generate_text_files(path, count):
    for _ in range(count):
        generate_text_file(path)