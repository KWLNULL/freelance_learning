import os

with open("drill1.txt","w",encoding="utf-8") as f:
    f.write("kwl is goat")
with open("drill1.txt","r",encoding="utf-8")as f:
    text=f.read()
    print(text)