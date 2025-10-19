#make a merge function and and input directory output file and prefix
#check if file exist in directory or not
#if file exist and if it ends with .pdf and starts with some prefix then append that with merger
#if merge done then at the end write the out file in the merged pdf and print the no of pdf merged 


import os
from PyPDF2 import PdfMerger

def mergerfunction(input_dir,out_file,prefix):
    merger=PdfMerger()
    merged=0
    for file in os.listdir(input_dir):
        if file.lower().endswith(".pdf") and file.startswith(prefix):
            merger.append(os.path.join(input_dir,file))
            merged+=1
            print(f"added {file}")
    if merged==0:
        print("no file were added")
    else:
        merger.write("merged file")
        merger.close()
        print(f"total {merged} were added")
if __name__=="__main__":
    mergerfunction("testpdfs","prefixbasedmerged.pdf","file")