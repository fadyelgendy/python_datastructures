class Node(object):
    def __init__(self, val):
        self.data = val
        self.next = None
        self.prev = None

    def set_data(self, val):
        self.data = val

    def get_data(self):
        return self.data
    
    def set_next(self, next):
        self.next = next

    def get_next(self):
        return self.next
    
    def set_prev(self, prev):
        self.prev = prev

    def get_prev(self):
        return self.prev