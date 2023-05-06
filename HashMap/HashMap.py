class HashMap(object):
    def __init__(self):
        self.data = []

        for i in range(1000):
            self.data.append([None, None])
    
    # Add New entry to Hash map
    def add(self, key, val):
        index = self.hash(key=key)

        if self.contains(key=key) is True:
            self.data[index][1] = val

        self.data[index][0] = key
        self.data[index][1] = val

    # Get a given key value
    def get(self, key):
        if self.contains(key=key) is False:
            return -1
        
        index = self.hash(key)

        return self.data[index][1]
    
    # Check if key exists
    def contains(self, key):
        index = self.hash(key=key)

        if len(self.data[index]) == 0:
            return -1
        
        return self.data[index][0] == key
    
    # Remove a given key
    def remove(self, key):
        if self.contains(key=key) is False:
            return -1
        
        index = self.hash(key=key)
        target = self.data[index][1]

        self.data[index] = [None, None]

        return target
    
    # Hashing Function
    def hash(self, key):
        return key % 1000

    # Print Hash map content
    def print_hash_map(self):
        for entry in self.data:
            if len(entry) > 0 and entry[0] is not None:
                print(f"{entry[0]}\t=> {entry}")
