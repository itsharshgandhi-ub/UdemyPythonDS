'''
Created on Dec 21, 2018

@author: harsh
'''

class AVLNode(object):

    def __init__(self, data):
        self.data = data
        self.height = 0
        self.right = None
        self.left = None