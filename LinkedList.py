'''
Created on Dec 20, 2018

@author: harsh
'''
# class Node(object):
#     def __init__(self, data):
#         self.data = data
#         self.nextNode = None

from Node import Node1

class LinkedList(object):
    def __init__(self):
        self.head = None
        self.size = 0
        
    def insertStart(self,data):
        self.size+=1
        newNode = Node1(data)
        if self.head:
            newNode.nextNode = self.head
            self.head = newNode
        else:
            self.head = newNode
            
    def size11(self):
        return self.size
    
    def traverse(self):
        availableNode = self.head
        
        while availableNode:
            print(availableNode.data)
            availableNode = availableNode.nextNode
    
    def insertEnd(self,data):
        self.size +=1
        availableNode = self.head
        newNode = Node1(data)
        
        while availableNode.nextNode:
            availableNode = availableNode.nextNode
            
        availableNode.nextNode = newNode
    
    def remove(self,data):
        if self.head is None:
            return
        self.size -=1
        
        currentNode = self.head
        previousNode = None
        
        while currentNode.data != data:
            previousNode = currentNode
            currentNode = currentNode.nextNode
            
        if previousNode is None:
            self.head = currentNode.nextNode   
        else:
            previousNode.nextNode = currentNode.nextNode

linkedList = LinkedList()
linkedList.insertStart(10)
linkedList.insertEnd(100)
linkedList.insertStart(30)
linkedList.insertStart(20)
print(linkedList.size11())
linkedList.traverse()
linkedList.remove(30)
linkedList.traverse()


            