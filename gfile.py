import sys
import os
import random
import utils

def generate(gver, path, filetype, count):
    if gver == "2" and filetype != "random":
        path = os.path.join(path, filetype.upper())
    
    if filetype == "txt":
        utils.txt_generator.generate_text_files(path, count)
    
    if filetype == "doc":
        utils.doc_generator.generate_doc_files(path, count)
    
    if filetype == "docx":
        utils.docx_generator.generate_docx_files(path, count)
        
    if filetype == "png":
        utils.png_generator.generate_png_files(path, count)
        
    if filetype == "jpg":
        utils.jpg_generator.generate_jpg_files(path, count)
    
    if filetype == "zip":
        utils.zip_generator.generate_zip_files(path, count)
    
    if filetype == "xls":
        utils.xls_generator.generate_xls_files(path, count)
    
    if filetype == "xlsx":
        utils.xlsx_generator.generate_xlsx_files(path, count)
        
    if filetype == "pdf":
        utils.pdf_generator.generate_pdf_files(path, count)
        
    if filetype == "mp4":
        utils.mp4_generator.generate_mp4_files(path, count)
        
    if filetype == "random":
        for _ in range(count):
            generate(gver, path, random.choice(["txt", "doc", "docx", "png", "jpg", "zip", "xls", "xlsx", "pdf", "mp4"]), 1)

    if filetype == "all":
        for typ in ["txt", "doc", "docx", "png", "jpg", "zip", "xls", "xlsx", "pdf", "mp4"]:
            generate(gver, path, typ, count)
            
    if filetype == "fast":
        # ignore doc and mp4
        for _ in range(count):
            generate(gver, path, random.choice(["txt", "docx", "png", "jpg", "zip", "xls", "xlsx", "pdf"]), 1)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 gfile.py <path> [count] [filetype] [generator-version]")
        sys.exit(1)
        
    path = sys.argv[1]
    count = int(sys.argv[2]) if len(sys.argv) > 2 else 50
    filetype = sys.argv[3] if len(sys.argv) > 3 else "random"
    gver = sys.argv[4] if len(sys.argv) > 4 else "1"
    
    if not os.path.exists(path):
        print("Path does not exist")
        sys.exit(1)
    
    if count < 1:
        print("Count must be greater than 0")
        sys.exit(1)
    
    generate(gver, path, filetype, count)
    
    utils.flags.print()
    
    
    
    # if filetype == "random":
        