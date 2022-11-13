# with ffmpeg required
# 需要在 ./videodata/ 下放置一些视频文件
import ffmpeg
import os
from faker import Faker
import random

from utils.utils import get_flag
from utils.flags import flags

fake = Faker()
fontpath = "./fonts/NotoSansSC-Regular.otf"

def generate_mp4_file(path):
    if not os.path.exists(path):
        os.makedirs(path)
    # 随机读取 ./videodata/ 下的一个视频文件
    video = random.choice(os.listdir("./videodata/"))
    filename = fake.name().replace(" ", "_") + f"_{random.randint(1000,9999)}" + ".mp4"
    # 生成随机水印文字
    watermark = get_flag()
    # 生成水印视频
    (
        ffmpeg.input(os.path.join("./videodata/", video))
        .output(
            os.path.join(path, filename),
            vf=f"drawtext=fontfile={fontpath}: text='{watermark}':y=line_h:x=line_h:fontsize=h/10:fontcolor=white:shadowy=2",
            ss=0,
            to="00:00:10",
            v="quiet",
            )
        .run()
    )
    return os.path.join(path, filename), watermark

def generate_mp4_files(path, count):
    for _ in range(count):
        flags.add(generate_mp4_file(path))