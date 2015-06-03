'''The function recurPower(base, exp) from Problem 2 computed baseexp by decomposing the problem into one recursive case and 
one base case:

baseexpbaseexp==base⋅baseexp−11ifexp>0ifexp=0
Another way to solve this problem just using multiplication (and remainder) is to note that

baseexpbaseexpbaseexp===(base2)exp2base⋅baseexp−11ifexp>0andexpisevenifexp>0andexpisoddifexp=0

Write a procedure recurPowerNew which recursively computes exponentials using this idea.
'''

def recurPowerNew(base, exp):
    '''
    base: int or float.
    exp: int >= 0

    returns: int or float; base^exp
    '''
    # Your code here
    if exp==0:
        return 1
    elif exp%2==0:
        return recurPowerNew(base*base,exp/2)
    elif exp%2!=0:
        return base*recurPowerNew(base,exp-1)

