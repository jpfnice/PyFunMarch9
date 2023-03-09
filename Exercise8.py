
def addList(li1, li2, default=0):
    """
    Parameters
    ----------
    li1 : a list of numbers
        
    li2 : a list of numbers
    
    default : a value to be added in case the 2 lists are
    not of the same size. The default is 0.

    Returns
    -------
     a list (the addition of the 2 lists received as argument elements 
     by elements)

    """
    
    li1_tmp=li1.copy() # li1_tmp=li1[:]
    li2_tmp=li2.copy()
    
    if len(li1) < len(li2):
        # [0] * 4 -> [0,0,0,0]
        li1_tmp.extend([default]*(len(li2)-len(li1)))
        
    elif len(li2) < len(li1):
        li2_tmp.extend([default]*(len(li1)-len(li2)))   
    
    #return [ li1_tmp[i] + li2_tmp[i] for i in range(len(li1_tmp)) ]

    res=[]
    ix=0
    while ix < len(li1_tmp):
        res.append(li1_tmp[ix]+li2_tmp[ix])
        ix=ix+1
        
    return res


l1=[1,2,3]
l2=[4,5,6,7,8]

l3=addList(l1,l2,2)

print(l3) # [5,7,9,9,10]

l1=[1,2,3,7,8]
l2=[10,20,30]

l3=addList(l1,l2)

print(l3) # [11,22,33,7,8]