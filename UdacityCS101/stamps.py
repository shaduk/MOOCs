# Define a procedure, stamps, which takes as its input a positive integer in
# pence and returns the number of 5p, 2p and 1p stamps (p is pence) required 
# to make up that value. The return value should be a tuple of three numbers 
# (that is, your return statement should be followed by the number of 5p,
# the number of 2p, and the nuber of 1p stamps).
#
# Your answer should use as few total stamps as possible by first using as 
# many 5p stamps as possible, then 2 pence stamps and finally 1p stamps as 
# needed to make up the total.
#
# (No fair for USians to just say use a "Forever" stamp and be done with it!)
#
def diff1(a):
    return a-5*(a/5),a/5

def diff2(b):
    return b-2*(b/2),b/2

def stamps(a):
    if(a>5):
        i,j = diff1(a)
        if(i>=0):
            k,m = diff2(i)
            if(k==1):
                return j,m,k
            else:
                return j,m,0
         
                
    if(a<5):
        k,m = diff2(a)
        if(k==1):
          return 0,m,k
        else:
          return 0,m,0
    else:
        return 1,0,0
        
         
    
print stamps(50)

print stamps(8)
#>>> (1, 1, 1)  # one 5p stamp, one 2p stamp and one 1p stamp
print stamps(5)
#>>> (1, 0, 0)  # one 5p stamp, no 2p stamps and no 1p stamps
print stamps(29)
#>>> (5, 2, 0)  # five 5p stamps, two 2p stamps and no 1p stamps
print stamps(0)
#>>> (0, 0, 0) # no 5p stamps, no 2p stamps and no 1p stamps