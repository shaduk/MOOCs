

class Stack:
    
    def __init__(self):
        self.items = []
        
    def push(self,item):
        self.items.append(item)
        
    def isEmpty(self):
        return self.items == []
        
    def pop(self):
        return self.items.pop()
        
    def peek(self):
        return self.items[len(self.items)-1]
        
    def size(self):
        return len(self.items)
        
        
#Implemented by me

def divideby2(number):
    remstack = Stack()
    temp = number
    while(temp!=1):
        rem = temp%2
        remstack.push(rem)
        temp = temp/2
        
    binString = "1"
    while not remstack.isEmpty():
        binString = binString + str(remstack.pop())

    return binString
    
print(divideby2(42))
