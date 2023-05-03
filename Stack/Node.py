class Node(object):
    def __init__(self, val):
        self.val = val
        self.next = None

    def get_value(self):
        return self.val
    
    def get_next(self):
        return self.next
    
    def set_next(self, next):
        self.next = next