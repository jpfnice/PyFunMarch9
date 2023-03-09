class Point: # __new__(), __init__(), __repr__(), ...
    def __init__(self, valx, valy):
        self.x=valx # definition of the attribute x
        self.y=valy # definition of the attribute y
    def __repr__(self): # should return string
        return f"<{self.x},{self.y}>"
    def __add__(self, other):
        return Point(self.x+other.x, self.y+other.y)

data=[5,6,7]
data.append(18) # append(data, 18)
    
p1=Point(3,5)
# 1) p1=Point.__new__()
# 2) p1.__init__(2,3)
# 3) __init__(p1,2,3)

p2=Point(4,5)

print(p1) # <2,3>
# 1) print(str(p1))
# 2) print(p1.__repr__())

print(p2) # <4,5>

print(p1.x) # 2
p1.x=7
print(p1) # <7,3>

p3=p1+p2
# 1) p3=p1.__add__(p2)

print(p3) # <11, 8>

if p1 == p2:
    print("Equal")
    
result=p1.distance(p2)
print(result)

p1.clear()
print(p1) # <0,0>


