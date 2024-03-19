class Stack:
    def __init__(self):
        self.list = []

    def __str__(self):
        values = self.list.reserve()
        vlues = [str(x) for x in self.list]
        return '\n'.join(values)
    
    def isEmpty(self):
        if self.list == []:
            return True
        else:
            return False

    def push(self, value):
        self.list.append(value)
        return "The element has been successfully inserted"

    def pop(self):
        if self.isEmpty():
            return "There is not any element in the stack"
        else:
            return self.list.pop()

def find_min(stack):
    if stack.isEmpty():
        return "Stack is empty"
    min_value = float('inf')  
    for element in stack.list:
        if element < min_value:
                min_value = element
    return min_value
        

customStack = Stack()
customStack.push(5)
min_value = find_min(customStack)
print("Minimum value: ", min_value)   
customStack.push(6)
min_value = find_min(customStack)
print("Minimum value: ", min_value)  
customStack.push(3)
min_value = find_min(customStack)
print("Minimum value: ", min_value)  
customStack.push(7)
min_value = find_min(customStack)
print("Minimum value: ", min_value)  
customStack.pop()
min_value = find_min(customStack)
print("Minimum value: ", min_value)  
customStack.pop()
min_value = find_min(customStack)
print("Minimum value: ", min_value)  

