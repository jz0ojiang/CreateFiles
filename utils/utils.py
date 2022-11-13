import random
import string

def get_flag():
    return f"flag{'{'+ ''.join(random.choices(string.ascii_letters + string.digits, k=8)) + '}'}"

class Flags():
    def __init__(self):
        self.flags = []

    def add(self, data):
        self.flags.append({"path": data[0], "flag": data[1]})

    def print(self):
        max_len = max([len(i["path"]) for i in self.flags])
        for i in self.flags:
            print(i["path"].replace("/", "\\").ljust(max_len), "\t\t", i["flag"])