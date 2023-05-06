from DoublyLinkedList import DoublyLinkedList

class Queue(object):
    def __init__(self):
        self.data = DoublyLinkedList()
    
    def is_empty(self):
        return self.data.get_size() == 0
    
    def size(self):
        return self.data.get_size()
    
    def peek(self):
        return self.data.get_tail()
    
    def enqueue(self, val):
        self.data.add(val)

    def dequeue(self):
        return self.data.remove()