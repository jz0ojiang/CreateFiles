import random
from faker import Faker
import xlwt
import os

from utils.utils import get_flag
from utils.flags import flags

fake = Faker()

def generate_xls_file(path):
    if not os.path.exists(path):
        os.makedirs(path)
    filename = fake.name().replace(" ", "_") + f"_{random.randint(1000,9999)}" + ".xls"
    flag = get_flag()
    workbook = xlwt.Workbook(encoding="utf-8")  # 实例化book对象
    sheet = workbook.add_sheet("Sheet1")  # 生成sheet
    sheet.write(0, 0, flag)
    workbook.save(os.path.join(path, filename))
    return os.path.join(path, filename), flag

def generate_xls_files(path, count):
    for _ in range(count):
        flags.add(generate_xls_file(path))
