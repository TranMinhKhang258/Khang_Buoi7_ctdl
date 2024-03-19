class Node:
    def _init__(self, value=None):
        self.value = value
        self.next = None
    def _str_(self): 
        return str(self.value)
class LinkedList:
    def _init__(self):
        self.head = None
        self.tail = None
    def _iter_(self): 
        curNode = self.head 
        while curNode: 
            yield curNode 
            curNode = curNode.next