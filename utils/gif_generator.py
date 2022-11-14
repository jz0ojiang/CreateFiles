from PIL import Image,ImageFont,ImageDraw,ImageSequence
from faker import Faker

import os
import random

from utils.utils import get_flag
from utils.flags import flags

fake = Faker()


def watermark_on_gif(in_gif,out_gif,text='scratch8'):
    """本函数给gif动图加水印"""
    frames = []
    myfont = ImageFont.truetype("./fonts/NotoSansSC-Regular.otf", 25)
    im = Image.open(in_gif)
    water_im = Image.new("RGBA", im.size)
    draw = ImageDraw.Draw(water_im)     
    width,height = water_im.width,water_im.height
    fontsize = draw.textsize(text,font = myfont) # 文字的宽度和高度
    #draw.text(( width//2-fontsize[0]//2, height-fontsize[1]*4), text, font=myfont,fill='gray')
    #水印文字描边黑色
    draw.text(( width//2-fontsize[0]//2-1, height-fontsize[1]*4-1), text, font=myfont,fill=(0,0,0))
    draw.text(( 9.5, 9.5), text, font=myfont,fill=(255,255,255))
    draw.text(( width//2-fontsize[0], height//2-fontsize[1]), text, font=myfont,fill=(255,255,255))
    draw.text(( width-fontsize[0]-10, height-fontsize[1]-10), text, font=myfont,fill=(255,255,255))
           
    water_mask = water_im.convert("1").point(lambda x: min(x, 160))
    water_im.putalpha(water_mask) 

    #print(im.info)
    index = 0
    for frame in ImageSequence.Iterator(im):             # 迭代每一帧
        frame = frame.convert("RGBA")
        #frame = Image.alpha_composite(frame,water_im)
        frame.paste(water_im,None,water_mask)
        frames.append(frame)
    newgif = frames[0]
    newgif.save(out_gif, save_all=True,append_images=frames[1:], quality=85,duration=100)
    im.close()


def generate_gif_file(path):
    if not os.path.exists(path):
        os.makedirs(path)
    # 随机读取 ./source/gif/ 下的一个gif文件
    gif = random.choice(os.listdir("./source/gif/"))
    filename = fake.name().replace(" ", "_") + f"_{random.randint(1000,9999)}" + ".gif"
    watermark = get_flag()
    watermark_on_gif(os.path.join("./source/gif/", gif), os.path.join(path, filename), watermark)
    return os.path.join(path, filename), watermark

def generate_gif_files(path, count):
    for _ in range(count):
        flags.add(generate_gif_file(path))