import os

files=["file_1.txt","file_2.txt","missing.txt"]

for i in range(1,4):
    with open(f"file_{i}.txt","w") as f:
        f.write(f"the is file{i}")


with open("merged_drill.txt","w") as out:
    for f in files:
        if os.path.exists(f):
            out.write(open(f).read()+"\n\n")
        else:
            print(f"!! skipped missing file {f}")