
fic=open("numbers.txt")

for line in fic:
    nb=int(line)
    if nb < 0:
        continue
    print(nb, nb**2)

print("The end")