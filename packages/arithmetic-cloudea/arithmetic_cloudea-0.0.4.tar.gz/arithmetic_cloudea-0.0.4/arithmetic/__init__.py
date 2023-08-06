"""
Descripetions for module:
This is easy.
Will you like?
"""

def add(x,y,*other):
    """
    desctiptions for function add
    """
    sum=x+y
    for i in other:
        sum+=i
    return sum
def minus(x,y,*other):
    """
    desctiptions for function minus
    """
    sum=x-y
    for i in other:
        sum-=i
    return sum
def multiply(x,y,*other):
    """
    desctiptions for function multiply
    """
    sum=x*y
    for i in other:
        sum*=i
    return sum
def devide(x,y,*other):
    """
    desctiptions for function devides
    """
    sum=x/y
    for i in other:
        sum/=i
    return sum
