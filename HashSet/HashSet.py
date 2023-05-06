class HashSet(object):
    def __init__(self):
        self.data = []

        for i in range(1000):
            self.data.append(None)
    
    def contains(self, key):
        if len(self.data) == 0:
            return False
    
        index = self.hash(key)

        for i in self.data:
            if i == index:
                return True
        
        return False
    
    def add(self, val):
        if self.contains(val):
            return
        
        index = self.hash(val)
        self.data[index] = val

    def remove(self, val):
        if self.contains(val) is False:
            return -1
        
        index = self.hash(val=val)
        target = self.data[index]

        del self.data[index]

        return target

    def hash(self, val):
        return val % 1000
    
    def print_hash_set(self):
        for i in self.data:
            if i is not None:
                print(f'{i} ', end='')
        
        print()