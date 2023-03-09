
import os
output=os.listdir(r"C:\Users\jpf\mar8")
print(output)

for filename in output:
    if filename.startswith("if"):
        print(filename)