from Node import Node

class DoublyLinkedList(object):
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def add_head(self, val):
        new_node = Node(val)
        
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.set_next(self.head)
            self.head.set_prev(new_node)
            self.head = new_node

        self.size = self.size + 1

    def add_tail(self, val):
        new_node = Node(val)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.set_next(new_node)
            new_node.set_prev(self.tail)
            self.tail = new_node
        
        self.size = self.size + 1
    
    def add_at(self, index, val):
        new_node = Node(val)
        current = self.head

        # Index = 0
        if index == 0 :
            self.add_head(val)
            return
        
        # Index = tail
        if index == self.size - 1:
            self.add_tail(val)
            return

        i = 0
        while current is not None:
            if i == index -1:
                next = current.get_next()
                next.set_prev(new_node)
                current.set_next(new_node)
                new_node.set_prev(current)
                new_node.set_next(next)
                break
            else:
                current = current.get_next()

            i = i + 1
        
        self.size = self.size + 1

    def remove(self, val):
        current = self.head
        prev = None
        target = None

        # remove at head
        if current.get_data() == val:
            target = current
            self.head = current.get_next()
            self.head.set_prev(None)
            target.set_next(None)
            target.set_prev(None)
            self.size = self.size - 1

            return target.get_data()
        
        # remove at tail
        if self.tail.get_data() == val:
            target = self.tail
            self.tail = self.tail.get_prev()
            self.tail.set_next(None)
            target.set_next(None)
            target.set_prev(None)
            self.size = self.size - 1

            return target.get_data()

        while current is not None:
            if current.get_data() == val:
                prev = current.get_prev()
                target = current
                current = current.get_next()
                prev.set_next(current)
                current.set_prev(prev)
                target.set_next(None)
                target.set_prev(None)
                break
            else:
                current = current.get_next()
            
        self.size = self.size - 1

        return target.get_data()


    def get_size(self):
        return self.size

    def print_list(self):
        current = self.head

        print(f'[HEAD]==>', end='')

        while current is not None:
            print(f'[ {current.get_data()} ]==>', end='')
            current = current.get_next()
        
        print('[TAIL]')

    def print_list_reverse(self):
        current = self.tail

        print(f'[TAIL]', end='')

        while current is not None:
            print(f'<==[ {current.get_data()} ]', end='')
            current = current.get_prev()
        
        print('<==[HEAD]')

