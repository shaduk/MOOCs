'''Write a simple procedure, myLog(x, b), that computes the logarithm of a number x relative to a base b. For example, if x = 16 and b = 2, then the result is 4 - because 24=16. If x = 15 and b = 3, then the result is 2 - because 32 is the largest power of 3 less than 15.

In other words, myLog should return the largest power of b such that b to that power is still less than or equal to x.

x and b are both positive integers; b is an integer greater than or equal to 2. Your function should return an integer answer.

Do not use Python's log functions; instead, please use an iterative or recursive solution to this problem that uses simple arithmatic operators and conditional testing.

Note: You will only get ten checks. Use these judiciously.
'''

def myLog(x, b):
    '''
    x: a positive integer
    b: a positive integer; b >= 2

    returns: log_b(x), or, the logarithm of x relative to a base b.
    '''
    # Your Code Here
    ans = 0
    while(ans<x):
        if b**(ans+1)>x and b**(ans)<=x:
            return ans
        
        ans = ans + 1