import random


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
        

class Printer:
    
    def __init__(self,ppm):
        self.pagerate = ppm
        self.currentTask = None
        self.timeRemaining = 0
        
    def tick(self):
        
        if self.currentTask != None:
            self.timeRemaining = self.timeRemaining - 1
            if self.timeRemaining <= 0:
                self.currentTask = None
                
    def busy(self):
        if self.currentTask != None:
            return True
        else:
            return False

    def startNext(self,newtask):
        self.currentTask = newtask
        self.timeRemaining = newtask.getPages()*60/self.pagerate
        
