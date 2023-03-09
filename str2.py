
name="Julia" # len() for in [] [:]

print(len(name))

for c in name:
    print(c)

print(name[1])
print(name[1:3])

name=name.upper()
print(name)

name="    data     "
print(name, len(name))
name=name.strip()
print(name, len(name))
name="-----data-23----"
print(name, len(name))
name=name.strip("-")
print(name, len(name))

name="12;45,78;79,98,100"
print(name, len(name))
name=name.replace(",", ";")
print(name, len(name))
result=name.split(";")
print(result)
total=0
for e in result:
    total = total + int(e) # 0 + int('12') => 0 + 12
print(total)

name="-".join(result)
print(name)

path="c:/temp/im1.jpg"

if path.endswith("jpg"):
    print("This is a JPEG file")
    
print("am" in path)



