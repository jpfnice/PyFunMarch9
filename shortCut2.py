data=[2,3,-4,5,16,-17,24,5,2]
res=[e**2 if e>0 else e for e in data] # a "list comprehension"
print(res)

nb=-45

if nb > 0:
    nb_abs= nb
else:
    nb_abs= -nb
    
print(nb, nb_abs)

nb_abs= nb if nb>0 else -nb # "if" shortcut

print(nb, nb_abs)
