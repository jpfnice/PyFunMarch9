
def isPrime(value):
    """
    Definition:
        
        A natural number (i.e. an int) is called a prime number 
        (or a prime) if it is greater than 1 and cannot be written 
        as the product of two smaller natural numbers. 
        
    How to implement the function:  
        
    To determine if "value" is prime number or not you
    could:
        1) verify that "value" is an int 
            (you could use isinstance() to test that)
        2) verify that "value" is > 1
            (you could use something like "if value > 1..." )
        3) verify that you cannot divide "value" by: 
            2, 3, 4, 5, ... ,value-1
            (you could use a loop and within the loop use % to
             get the remainder of the division of "value" by a
             given number)
    If this 3 conditions are satisfied, you can return
    True: "value" is a Prime number
    Otherwise you should return False

    """
    if not isinstance(value, int):
        return False
    
    if value <= 1:
        return False
    
    divisor=2
    while divisor < value:
        if value % divisor == 0:
            return False
        divisor += 1
        
    return True


test=[1,2,3,4,5,7,17,21,23,45,278,2771]

for e in test:
    if isPrime(e):
        print(f"{e} is a prime number")
    else:
        print(f"{e} is not a prime number")