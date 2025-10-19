import os
keyword="KWL GOAT"
files=["file1.txt","file2.txt","file3.txt"]

for i,name in enumerate(files,start=1):
    with open(name,"w") as f:
        f.write(f"this is {name} and might contain the keyowrd")
        if i%2==0:
            f.write(f"\n\n {keyword}")
with open("keyword_merged.txt","w") as out:
    for f in files:
        if os.path.exists(f):
            content=open(f,"r").read()
            if keyword in content:
                out.write(content + "\n\n")
            else:
                print(f"keyword not found in {f}")
        else:
            print("file doesn't exist")
print("keyword based merger done")
