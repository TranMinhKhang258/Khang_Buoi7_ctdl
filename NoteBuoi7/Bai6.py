class Stack:
    def __init__(self, maxSize):
        self.maxSize = maxSize
        self.list = []

    def __str__(self):
        values = self.list.reverse()
        values = [str(x) for x in self.list]
        return '\n'.join(values)

    def isEmpty(self):
        if self.list == []:
            return True
        else:
            return False
        
    def isFull(self):
        if len(self.list) == self.maxSize:
            return True
        else:
            return False
        
    def push(self, value):
        self.list.append(value)
        return "The element has been successfully inserted"
    
    def delete(self):
        self.list = None

customStack = Stack(4)
customStack.push(1)
customStack.push(2)
customStack.push(3)
print(customStack)
print(customStack.isFull())
