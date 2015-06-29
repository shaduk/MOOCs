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
    
def hotPotato(namelist,num):
    q = Queue()
    
    for name in namelist:
        q.enqueue(name)
    
    while q.size()>1:
        print q.view()
        for i in range(num):
            q.enqueue(q.dequeue())
        q.dequeue()
        
    return q.dequeue()
    
print(hotPotato(["Bill","David","Susan","Jane","Kent","Brad"],7))
