# ------------
# User Instructions
#
# Define a function, all_ints(), that generates the 
# integers in the order 0, +1, -1, +2, -2, ...

def ints(start, end = None):
    i = start
    while i <= end or end is None:
        yield i
        i = i + 1
    

def all_ints():
    "Generate integers in the order 0, +1, -1, +2, -2, +3, -3, ..."
    # Your code here.
    i = 0
    sign = -1
    while True:
        yield i
        if sign== -1:
            i = abs(i) + 1
        sign = -1*sign
        i = sign*i
        
        
L = all_ints()
