'''
Created on Dec 21, 2018

@author: harsh
'''

class StackImplementation(object):
   
    def __init__(self):
        self.stack = []
    
    def isEmpty(self):
        return self.stack == []
    
    def stackPush(self,data):
        self.stack.append(data)
    
    def stackPeek(self):
        return self.stack[-1]
    
    def stackPop(self):
        toReturn = self.stack[-1]
        del self.stack[-1]
        return toReturn
    def stackSize(self):
        return len(self.stack)
    
st = StackImplementation()
st.stackPush(10)
print(st.stackPeek())
print(st.stackSize())
print(st.isEmpty())
print(st.stackPop())
print(st.stackSize())