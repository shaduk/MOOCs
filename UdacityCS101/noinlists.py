# Numbers in lists by SeanMc from forums
# define a procedure that takes in a string of numbers from 1-9 and
# outputs a list with the following parameters:
# Every number in the string should be inserted into the list.
# If a number x in the string is less than or equal 
# to the preceding number y, the number x should be inserted 
# into a sublist. Continue adding the following numbers to the 
# sublist until reaching a number z that
# is greater than the number y. 
# Then add this number z to the normal list and continue.

#Hint - "int()" turns a string's element into a number

def numbers_in_lists(string):
    ans = []
    templist = map(int,list(string))
    ans.append(templist[0])
    for i in range(1,len(templist)):
       
        if templist[i]<=templist[i-1] and isinstance(ans[len(ans)-1], list):
            ans[len(ans)-1].append(templist[i])
        elif templist[i]<=templist[i-1] and type(ans[len(ans)-1])!='list':
            ans.append([templist[i]])
        else:
            ans.append(templist[i])
    return ans
    
   


#testcases
string = '543987'
result = [5,[4,3],9,[8,7]]

print numbers_in_lists(string)

print repr(string), numbers_in_lists(string) == result
string= '987654321'
result = [9,[8,7,6,5,4,3,2,1]]
print repr(string), numbers_in_lists(string) == result
string = '455532123266'
print numbers_in_lists(string)
result = [4, 5, [5, 5, 3, 2, 1, 2, 3, 2], 6, [6]]
print repr(string), numbers_in_lists(string) == result
string = '123456789'
result = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print repr(string), numbers_in_lists(string) == result