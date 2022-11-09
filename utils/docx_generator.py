from docx import Document
from faker import Faker
import os

from utils.utils import get_flag

fake = Faker()

def generate_docx_file(path):
    if not os.path.exists(path):
        os.makedirs(path)
    filename = fake.name().replace(" ", "_") + ".docx"
    document = Document()
    document.add_paragraph(get_flag())
    document.add_paragraph(fake.text())
    document.save(os.path.join(path, filename))
    return os.path.join(path, filename)

def generate_docx_files(path, count):
    for _ in range(count):
        generate_docx_file(path)