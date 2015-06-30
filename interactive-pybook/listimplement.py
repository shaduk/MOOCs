class Node:
    
    def __init__(self,initdata):
        self.data = initdata
        self.next = None
        
    def getData(self):
        return self.data
      
    def setData(self,newdata):
        self.data = newdata
        
    def getNext(self):
        return self.next
        
    def setNext(self,newnext):
        self.next = newnext
        
    
temp = Node(23)
print temp.getData()
