
def add(op1, op2):
    if isinstance(op1, (int, float)) and isinstance(op2, (int, float)):
        temp=op1 + op2 # temp is a local variable
        return temp
    else:
        print("Wrong kind of arguments received")
        return None


result=add(56, 78)
print(result)

result=add(56, 100)
print(result)

result=add("56", "100")
print(result)

