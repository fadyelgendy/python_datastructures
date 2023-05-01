from Node import Node


class LinkedList:
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
            new_node.next = self.head
            self.head = new_node

        self.size = self.size + 1

    def add_tail(self, val):
        new_node = Node(val)
        self.tail.next = new_node
        self.tail = new_node

        self.size = self.size + 1

    def add_at(self, val, index):
        current = self.head
        new_node = Node(val)

        i = 0
        while current is not None:
            if i is index - 1:
                break
            else:
                current = current.next

            i = i + 1
        
        new_node.next = current.next
        current.next = new_node

        self.size = self.size + 1

    def remove(self, val):
        target = None
        current = self.head
        prev = None

        while current is not None:
            if current.data is val:
                target = current
                current = current.next
                prev.next = current
                target.next = None
                break
            else:
                prev = current
                current = current.next
        
        print(f"[ {target.data}] is removed!")
        self.size = self.size - 1

    def print_list(self):
        current = self.head

        print(f'[ HEAD ]-->', end='')

        while current is not None:
            print(f'[ {current.data} ]-->', end='')
            current = current.next

        print(f'[ TAIL ]')

        print(f'Total Nodes: [ {self.size} ]')
