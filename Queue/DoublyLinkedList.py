from Node import Node

class DoublyLinkedList(object):
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def add(self, val):
        new_node = Node(val=val)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.set_next(self.head)
            self.head.set_prev(new_node)
            self.head = new_node
        
        self.size = self.size + 1
    
    def remove(self):
        if self.tail is None:
            return -1
        
        target = self.tail
        self.tail = self.tail.get_prev()
        target.set_prev(None)
        target.set_next(None)

        self.size = self.size - 1

        return target.get_data()
    
    def get_tail(self):
        if self.tail is None:
            return -1
        
        return self.tail.get_data()
    
    def get_size(self):
        return self.size