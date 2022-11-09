# with libreoffice required

import os
from docx import Document
from faker import Faker

from utils.utils import get_flag

fake = Faker()

def generate_doc_file(path):
    if not os.path.exists(path):
        os.makedirs(path)
    filename = fake.name().replace(" ", "_") + ".docx"
    document = Document()
    document.add_paragraph(get_flag())
    document.add_paragraph(fake.text())
    if not os.path.exists("./temp/"):
        os.makedirs("./temp/")
    document.save("./temp/" + filename)
    
    os.system(f"soffice --headless --convert-to doc ./temp/{filename} --outdir {path}")
    os.remove("./temp/" + filename)
    return os.path.join(path, filename)

def generate_doc_files(path, count):
    for _ in range(count):
        generate_doc_file(path)