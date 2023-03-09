
data=[2,3,-4,5,16,-17,24,5,2]

res=[]
for e in data:
    res.append(e**2)
print(res)

res=[e**2 for e in data] # a "list comprehension"
print(res)

res=[]
for e in data:
    if e > 0:
        res.append(e**2)
print(res)

res=[e**2 for e in data if e > 0] # a "list comprehension"
print(res)



res={e**2 for e in data if e > 0} # a "set comprehension"
print(res)

