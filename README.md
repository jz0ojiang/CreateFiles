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
- gif

## 使用方法

```bash
python3 gfile.py <path> [count] [filetype] [generator-version]
```

- path: 生成文件的路径

- count: 生成文件的数量，默认为 50

- filetype: 生成文件的类型，默认为 random

- generator-version: 生成文件的版本，默认为 1

## 生成文件的类型

`txt, png, jpg, mp4, pdf, xls, xlsx, doc, docx, zip, gif` 等为指定类型

`random` 为随机类型

`all` 为所有类型，此时 count 参数变为每个类型生成的数量

`fast` 为快速随机生成，将排除 doc, mp4 等较慢的文件类型（正好这俩类型需要外部依赖）

## 生成文件的版本

- 1 (默认): 生成的文件直接存入指定路径

- 2 : 生成的文件将在 指定路径/文件类型/ 下存储

## 输出

生成结束后，会在终端输出生成文件的路径与flag

```
.\output\Luis_Carter_9052.docx                   flag{wMOPoVGD}
.\output\Kelly_Castillo_8321.png                 flag{7zhGZTEq}
.\output\Andrew_Mendoza_4096.png                 flag{USlp7rhX}
.\output\Omar_Morton_1785.xls                    flag{Rs668aVb}
.\output\Jacob_Mitchell_4978.png                 flag{EfYVOCmq}
.\output\Robert_Booker_4562.xlsx                 flag{WipX0jke}
...
```