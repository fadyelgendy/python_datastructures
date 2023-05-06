class HashSet(object):
    def __init__(self):
        self.data = []

        for i in range(1000):
            self.data.append(None)
    
    def contains(self, key):
        if len(self.data) == 0:
            return False
    
        index = self.hash(key)
        return self.data[index] != None
    
    def add(self, key, val):
        index = self.hash(key)
        if self.contains(key):
            self.data[index] = val
        
        self.data[index] = val

    def remove(self, key):
        if self.contains(key) is False:
            return -1
        
        index = self.hash(key)
        target = self.data[index]

        self.data[index] = None

        return target
    
    def get(self, key):
        if self.contains(key) is False:
            return -1
        
        index = self.hash(key)
        return self.data[index]

    def hash(self, val):
        return val % 1000
    
    def print_hash_set(self):
        for indx,val in enumerate(self.data):
            if self.data[indx] is not None:
                print(f"{indx}\t=>\t{self.data[indx]}")
        