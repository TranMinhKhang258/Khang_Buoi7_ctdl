# class Node:
    ## WRITE NODE CONSTRUCTOR HERE ##
    #                               #
    #                               #

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    #                               #
    #                               #
    #################################
        
# class Stack:
    ## WRITE STACK CONSTRUCTOR HERE ##
    #                                #
    #                                #
        
class Stack:
    def __init__(self, value=None):
        if value is not None:
            self.top = Node(value)
            self.height = 1
        else:
            self.top = None
            self.height = 0

    #                                #
    #                                #
    ##################################




my_stack = Stack(4)

print('Top:', my_stack.top.value)
print('Height:', my_stack.height)



"""
    EXPECTED OUTPUT:
    ----------------
    Top: 4
    Height: 1

"""