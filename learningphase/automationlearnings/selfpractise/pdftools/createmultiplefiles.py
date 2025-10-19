import os

for i in range(1,4):
    with open(f"file_{i}.txt","w") as f:
        f.write(f"the is file{i}")
print("done")