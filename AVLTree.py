'''
Created on Dec 21, 2018

@author: harsh
'''

class AVLTree(object):
    
    def __init__(self):
        self.root = None
    def calculateHeight(self,node):
        if not node:
            return -1
        else:
            return node.height
        
#     if it returns >1 then right rotation is to be performed on the tree
#     if -1 is returned, then left rotation is to be performed
    def calculateBalance(self,node):
        if not node:
            return 0
        else:
            return self.calculateHeight(node.left())  - self.calculateHeight(node.right)
        
#         draw and visualize :p
    def rotateRight(self,node):
        tempLeft = node.left
        tempRight = node.left.right
        
        tempLeft.right = node
        node.left = tempRight
        node.height = max(self.calculateHeight(node.left),self.calculateHeight(node.right))+1
        tempLeft.height  = max(self.calculateHeight(tempLeft.left),self.calculateHeight(tempLeft.right))+1
        
        return tempLeft
    def rotateLeft(self,node):
        tempRight = node.right
        templeft = node.right.right
        
        tempRight.left = node
        node.right = templeft
        node.height = max(self.calculateHeight(node.left),self.calculateHeight(node.right))+1
        tempRight.height  = max(self.calculateHeight(tempRight.left),self.calculateHeight(tempRight.right))+1
        
        return tempRight