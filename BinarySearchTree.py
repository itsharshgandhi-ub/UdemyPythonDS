'''
Created on Dec 21, 2018

@author: harsh
'''
from TreeNode import TreeNode

class BinarySearchTree(object):
    
    def __init__(self):
        self.root =None
    def insert(self,data):
        if not self.root:
            self.root = TreeNode(data)
        else:
            self.insertNode(data,self.root)
    
    def insertNode(self,data,node):
        if data>node.data:
            if node.right:
                self.insertNode(data, node.right)
            else:
                node.right = TreeNode(data)
        else:
            if node.left:
                self.insertNode(data, node.left)
            else:
                node.left = TreeNode(data)
    def getMin(self):
        if not self.root:
            return
        actualNode = self.root
        while actualNode.left:
            actualNode = actualNode.left
        return actualNode.data
    def getMax(self):
        if not self.root:
            return
        actualNode = self.root
        while actualNode.right:
            actualNode = actualNode.right
        return actualNode.data
    def traverseInorder(self):
        if self.root:
            self.inorder(self.root)
    def inorder(self,node):
        if node.left:
            self.inorder(node.left)
        print(node.data)
        if node.right:
            self.inorder(node.right)

bst = BinarySearchTree()
bst.insert(20)
bst.insert(5)
bst.insert(10)
bst.insert(30)
bst.traverseInorder()
print(bst.getMax())
print(bst.getMin())