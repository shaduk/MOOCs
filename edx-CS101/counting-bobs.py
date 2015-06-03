'''Assume s is a string of lower case characters.

Write a program that prints the number of times the string 'bob' occurs in s. For example, if s = 'azcbobobegghakl', then your program should print

Number of times bob occurs is: 2
For problems such as these, do not include raw_input statements or define the variable s in any way. Our automated testing will provide a value of s for you - so the code you submit in the following box should assume s is already defined. 
If you are confused by this instruction, please review L4 Problems 10 and 11 before you begin this problem set.
'''

 # Paste your code into this box 
 
s = 'azcbobobegghakl'
count = -1
times = 0
for let in s:
    count = count +1
    if let=='b' and count<len(s)-2:
        if s[count]+s[count+1]+s[count+2] == 'bob':
            times= times + 1

print times
            