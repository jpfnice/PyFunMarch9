"""
New exercise:
     
Given a file with this format (you can use "data.txt" for instance):

    x1:0.34;x2:0.56
    x1:0.24;x2:0.45
    x1:0.27;x2:0.55
    ...

extract out of it the numerical values associated with x1 and x2.
The values associated with x1 will be stored in a list with the name X1.
The values associated with x2 will be stored in a list with the name X2.
    
To extract the 2 float out of the line you could:
    1) use slices
    2) use 2 split() methods
    3) use another strategy ??
    
    str methods that could help:
    split(), index(), strip(), replace(), ...
    a slice, ...
    the function len(), ...
    
Create a list Y1 that will contain the cosine of each value stored in X1 
(use the math.cos() function)

Create a list Y2 that will contain the sine of each value stored in X2 
(use the math.sin() function)

Once the 4 lists will be created I will show you how to plot the corresponding points (X1,Y1, X2,Y2).
"""

import math

X1=[]
X2=[]

f1=open("data.txt")

for line in f1:  #" 	x1:0.24;x2:0.58\n"
    line2=line.replace(";",":") #" 	x1:0.24:x2:0.58\n"
    result=line2.split(":") #  [" 	x1","0.24","x2","0.58\n"]
    if len(result) == 4:
        x1=float(result[1])  # "0.24"
        x2=float(result[3])  # "0.58\n" 
        X1.append(x1)
        X2.append(x2)
    else:
        print("Error parsing line:", line)
    
f1.close()

print(X1)
print(X2)


Y1=[]
for e in X1:
    Y1.append(math.cos(e))
    
Y2=[]
for e in X2:
    Y2.append(math.sin(e))

print(Y1)
print(Y2)

# pip install matplotlib
# conda install matplotlib

import matplotlib.pyplot as plt

plt.plot(X1, Y1, label="Cosine")
plt.plot(X2, Y2, label="Sine")
plt.legend()
plt.show()