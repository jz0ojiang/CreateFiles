from faker import Faker
import xlwt
import os

from utils.utils import get_flag

fake = Faker()

def generate_xls_file(path):
    if not os.path.exists(path):
        os.makedirs(path)
    filename = fake.name().replace(" ", "_") + ".xls"
    workbook = xlwt.Workbook(encoding="utf-8")  # 实例化book对象
    sheet = workbook.add_sheet("Sheet1")  # 生成sheet
    sheet.write(0, 0, get_flag())
    workbook.save(os.path.join(path, filename))
    return os.path.join(path, filename)

def generate_xls_files(path, count):
    for _ in range(count):
        generate_xls_file(path)    
