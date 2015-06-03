'''
Suppose you are given two strings (they may be empty), s1 and s2. 
You would like to "lace" these strings together, by successively alternating elements of each string
(starting with the first character of s1). If one string is longer than the other, 
then the remaining elements of the longer string should simply be added at the end of the new string.
For example, if we lace 'abcd' and 'efghi', we would get the new string: 'aebfcgdhi'.

Write an iterative procedure, called laceStrings(s1, s2) that does this.
'''





def laceStrings(s1, s2):
    """
    s1 and s2 are strings.

    Returns a new str with elements of s1 and s2 interlaced,
    beginning with s1. If strings are not of same length, 
    then the extra elements should appear at the end.
    """
    # Your Code Here
    ans = ""
    if len(s2) >= len(s1):
        for i in range(len(s1)):
            ans = ans + s1[i]
            ans = ans + s2[i]
        ans = ans + s2[len(s1):]
    else:
        for i in range(len(s2)):
            ans = ans + s1[i]
            ans = ans + s2[i]
        ans = ans + s1[len(s2):]   
    return ans