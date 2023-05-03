from Node import Node

class LinkedList(object):
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def add(self, val):
        node = Node(val)

        if self.head is None:
            self.head = node
            self.tail = node
        else:
            node.set_next(self.head)
            self.head = node

        self.size = self.size + 1
    
    def remove(self):
        if self.head is not None:
            target = self.head
            self.head = self.head.get_next()
            self.size = self.size - 1
            return target.get_value()
        
        return -1
    
    def get_head(self):
        if self.head is not None:
            return self.head.get_value()
        
        return -1
    
    def get_size(self):
        return self.size
