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
    
# Implemented by myself

    
def parChecker(symbol):
    s = Stack()
    for i in symbol:
        if i in '([{':
            s.push(i)
        elif i in ')]}':
            if s.isEmpty():
                return False
            else:
                top = s.pop()
            
    return s.isEmpty()
    
print(parChecker('{{([][])}()}'))
print(parChecker('[{()]}}'))   
    
# Implemented by the book

def parCheckerbook(symbolString):
    s = Stack()
    balanced = True
    index = 0
    while index < len(symbolString) and balanced:
        symbol = symbolString[index]
        if symbol in "([{":
            s.push(symbol)
        else:
            if s.isEmpty():
                balanced = False
            else:
                top = s.pop()
                if not matches(top,symbol):
                       balanced = False
        index = index + 1
    if balanced and s.isEmpty():
        return True
    else:
        return False

def matches(open,close):
    opens = "([{"
    closers = ")]}"
    return opens.index(open) == closers.index(close)
