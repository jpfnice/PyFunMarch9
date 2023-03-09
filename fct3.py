
def subtract(op1, op2):
    if isinstance(op1, (int, float)) and isinstance(op2, (int, float)):
        temp=op1 - op2 # temp is a local variable
        return temp
    else:
        print("Wrong kind of arguments received")
        return None


result=subtract(56, 78) # Positional arguments
print(result)

result=subtract(op2=56, op1=78) # named arguments
print(result)


