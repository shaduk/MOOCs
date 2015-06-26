class Queue:
    
    def __init__(self):
        self.items = []
        
    def isEmpty(self):
        return self.items==[]
        
    def enqueue(self,item):
        return self.items.insert(0,item)
        
    def dequeue(self):
        return self.items.pop()
        
    def size(self):
        return len(self.items)
        
    def view(self):
        return self.items
    
    
q = Queue()
q.enqueue(2)
q.enqueue(5)
q.enqueue(8)
q.dequeue()
print q.view()
print q.size()
        