from PIL import Image, ImageDraw, ImageFont
from faker import Faker
import os

from utils.utils import get_flag

fake = Faker()

def generate_png_file(path):
    if not os.path.exists(path):
        os.makedirs(path)
    filename = fake.name().replace(" ", "_") + ".png"
    img = Image.new('RGB', (400, 400), color = (73, 109, 137))
    d = ImageDraw.Draw(img)
    d.text((15,15), get_flag() + "\n" + fake.text(), fill=(255,255,0),font=ImageFont.truetype("./fonts/NotoSansSC-Regular.otf", 25))
    img.save(os.path.join(path, filename))
    return os.path.join(path, filename)

def generate_png_files(path, count):
    for _ in range(count):
        generate_png_file(path)