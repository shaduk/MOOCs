# Define a procedure, find_last, that takes as input
# two strings, a search string and a target string,
# and returns the last position in the search string
# where the target string appears, or -1 if there
# are no occurences.
#
# Example: find_last('aaaa', 'a') returns 3

# Make sure your procedure has a return statement.

def find_last(a,b):
    
    stop = 0
    while True:
        start = a.find(b,stop)
        if(start==-1):
            temp=-1
            break
        temp = stop
        stop = a.find(b,start+1)
        if(stop==-1):
            temp = start
            break
    return temp
    
        
       
        
        

print find_last('aaaa', 'a')
#>>> 3

print find_last('aaaaa', 'aa')
#>>> 3

print find_last('aaaa', 'b')
#>>> -1

print find_last("111111111", "1")
#>>> 8

print find_last("222222222", "")
#>>> 9

print find_last("", "3")
#>>> -1

print find_last("", "")
#>>> 0
