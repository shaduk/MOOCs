class Deque:
    
    def __init__(self):
        self.items = []
    
    def addFront(self,item):
        self.items.append(item)
        
    def addRear(self,item):
        self.items.insert(0,item)
        
    def removeFront(self):
        self.items.pop()
        
    def removeRear(self):
        self.items.pop(0)
        
    def isEmpty(self):
        return self.items == []
    
    def size(self):
        return len(self.items)
        
    def view(self):
        return self.items
    
q = Deque()
q.addFront(3)
q.addRear(4)
q.addRear(4)
q.addRear(6)
q.addRear(9)
q.addFront(9)
print q.view()
