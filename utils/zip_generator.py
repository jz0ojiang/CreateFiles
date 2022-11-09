import zipfile
import os
import random
from faker import Faker

import utils

fake = Faker()

def generate_zip_file(path):
    if not os.path.exists(path):
        os.makedirs(path)
    if not os.path.exists("./temp/"):
        os.makedirs("./temp/")
    filepath = random.choice([
        utils.txt_generator.generate_text_file,
        utils.docx_generator.generate_docx_file,
        utils.png_generator.generate_png_file,
        utils.jpg_generator.generate_jpg_file,
        utils.xls_generator.generate_xls_file,
        utils.xlsx_generator.generate_xlsx_file,
        utils.pdf_generator.generate_pdf_file,
    ])("./temp/")
    with zipfile.ZipFile(os.path.join(path, fake.name().replace(" ", "_") + ".zip"), "w", zipfile.ZIP_DEFLATED) as zip:
        zip.write(filepath, os.path.basename(filepath))
    os.remove(filepath)
    return os.path.join(path, os.path.basename(filepath))

def generate_zip_files(path, count):
    for _ in range(count):
        try:
            generate_zip_file(path)
        except:
            print("Error while generating zip file" + path)
            continue