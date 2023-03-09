
fic=open("data.txt")

total=0

for line in fic:
    result=line.split(",")
    for nb in result:
        if nb != "\n":
            total = total + int(nb)

print(total)

#text=fic.read()
#print(text)