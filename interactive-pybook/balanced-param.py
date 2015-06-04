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
        if i == '(':
            s.push(i)
        elif i==')':
            if s.isEmpty():
                return False
            else:
                s.pop()
    return s.isEmpty()
    
# Implemented by the book

def parCheckerbook(symbolString):
    s = Stack()
    balanced = True
    index = 0
    while index < len(symbolString) and balanced:
        symbol = symbolString[index]
        if symbol == "(":
            s.push(symbol)
        else:
            if s.isEmpty():
                balanced = False
            else:
                s.pop()

        index = index + 1

    if balanced and s.isEmpty():
        return True
    else:
        return False

        
print(parChecker('((()))'))
print(parChecker('(())()))))'))
print(parChecker('((()())'))