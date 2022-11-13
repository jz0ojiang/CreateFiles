from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from faker import Faker
import os
import random

from utils.utils import get_flag
from utils.flags import flags

fake = Faker()
fake_cn = Faker("zh_CN")

pdfmetrics.registerFont(TTFont('ZCOOLKuaiLe', "./fonts/ZCOOLKuaiLe-Regular.ttf"))

def generate_pdf_file(path):
    if not os.path.exists(path):
        os.makedirs(path)
    filename = fake.name().replace(" ", "_") + f"_{random.randint(1000,9999)}" + ".pdf"
    flag = get_flag()
    doc = SimpleDocTemplate(os.path.join(path, filename))
    styles = getSampleStyleSheet()
    styles["Normal"].fontName = "ZCOOLKuaiLe"
    story = []
    story.append(Paragraph(flag, styles["Heading1"]))
    if random.randint(0, 1):
        for _ in range(random.randint(1, 8)):
            if random.randint(0, 1):
                for text in fake.paragraphs(nb=random.randint(10,30), ext_word_list=None):
                    story.append(Paragraph(text, styles["Normal"]))
            else:
                for text in fake_cn.paragraphs(nb=random.randint(20,30), ext_word_list=None):
                    story.append(Paragraph(text, styles["Normal"]))
    doc.build(story)
    return os.path.join(path, filename), flag

def generate_pdf_files(path, count):
    for _ in range(count):
        flags.add(generate_pdf_file(path))