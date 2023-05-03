from LinkedList import LinkedList

class Stack(object):
    def __init__(self):
        self.data = LinkedList()
    
    def is_empty(self):
        return self.data.get_size() == 0
    
    def peek(self):
        return self.data.get_head()

    def size(self):
        return self.data.get_size()

    def push(self, val):
        self.data.add(val)

    def pop(self):
        return self.data.remove()
    
