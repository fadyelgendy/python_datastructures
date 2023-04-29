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

    def print_list(self):
        current = self.head

        print(f'[ HEAD ]-->', end='')

        while current is not None:
            print(f'[ {current.data} ]-->', end='')
            current = current.next

        print(f'[ TAIL ]')

        print(f'Total Nodes: [ {self.size} ]')
