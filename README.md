# CreateFiles

简易含 flag 文件生成器

支持文件：
- txt
- png
- jpg
- mp4 (需要 ffmpeg)
- pdf
- xls
- xlsx
- doc (需要 libreoffice)
- docx
- zip

## 使用方法

```bash
python3 gfile.py <path> [count] [filetype] [generator-version]
```

- path: 生成文件的路径

- count: 生成文件的数量，默认为 50

- filetype: 生成文件的类型，默认为 random

- generator-version: 生成文件的版本，默认为 1

## 生成文件的类型

`txt, png, jpg, mp4, pdf, xls, xlsx, doc, docx, zip` 等为指定类型

`random` 为随机类型

## 生成文件的版本

- 1 (默认): 生成的文件直接存入指定路径

- 2 : 生成的文件将在 指定路径/文件类型/ 下存储