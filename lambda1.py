import functools

line='23:56:78:12:34:78:100'

result=line.split(":")
print(result)

result2=[]
for e in result:
    result2.append(int(e))
print(result2)


result2=list(map(int, result))
print(result2)

data=[5,6,7,10,12,23]

def fct(a):
    return a**2

data2=list(map(fct, data))
print(data2)

def isEven(a):
    return a % 2 == 0

data2=list(filter(isEven, data))
print(data2)

def f1(a,b):
    return a*b

data2=functools.reduce(f1, data)
print(data2)






