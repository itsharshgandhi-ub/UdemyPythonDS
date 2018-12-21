'''
Created on Dec 21, 2018

@author: harsh
'''

class QueueImplementation(object):
   

    def __init__(self):
        self.queue = []
    def isEmpty(self):
        return self.queue ==[]
    def queueSize(self):
        return len(self.queue)
    def queuePeek(self):
        return self.queue[-1]
    def dequeue(self):
        toReturn = self.queue[0]
        del self.queue[0]
        return toReturn
    def enqueue(self,data):
        self.queue.append(data)

q = QueueImplementation()
q.enqueue(10)
q.enqueue(11)
q.enqueue(12)
print(q.queueSize())
print(q.dequeue())
print(q.queuePeek())
