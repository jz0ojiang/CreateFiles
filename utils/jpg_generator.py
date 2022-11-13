import random
from PIL import Image, ImageDraw, ImageFont
from faker import Faker
import os

from utils.utils import get_flag
from utils.flags import flags

fake = Faker()

def generate_jpg_file(path):
    if not os.path.exists(path):
        os.makedirs(path)
    filename = fake.name().replace(" ", "_") + f"_{random.randint(1000,9999)}" + ".jpg"
    flag = get_flag()
    img = Image.new('RGB', (600, 500), color = (73, 109, 137))
    d = ImageDraw.Draw(img)
    d.text((30,30), flag + "\n" + fake.text(), fill=(255,255,255),font=ImageFont.truetype("./fonts/NotoSansSC-Regular.otf", 25))
    img.save(os.path.join(path, filename))
    return os.path.join(path, filename), flag

def generate_jpg_files(path, count):
    for _ in range(count):
        flags.add(generate_jpg_file(path))