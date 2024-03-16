class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        

class Queue:
    def __init__(self, value):
        new_node = Node(value)
        self.first = new_node
        self.last = new_node
        self.length = 1

    def print_queue(self):
        temp = self.first
        while temp is not None:
            print(temp.value)
            temp = temp.next
        
    def enqueue(self, value):
        new_node = Node(value)
        if self.first is None:
            self.first = new_node
            self.last = new_node
        else:
            self.last.next = new_node
            self.last = new_node
        self.length += 1
        return True

    ## WRITE DEQUEUE METHOD HERE ##
    #                             #
    #                             #

    def dequeue(self):
        if self.first is None:
            return None
        else:
            dequeued_value = self.first.value
            self.first = self.first.next
            self.length -= 1
            if self.length == 0:
                self.last = None
            return dequeued_value

    #                             #
    #                             #
    ###############################

 

 
my_queue = Queue(1)
my_queue.enqueue(2)

# (2) Items - Returns 2 Node
print(my_queue.dequeue())
# (1) Item -  Returns 1 Node
print(my_queue.dequeue())
# (0) Items - Returns None
print(my_queue.dequeue())



"""
    EXPECTED OUTPUT:
    ----------------
    1
    2
    None

"""