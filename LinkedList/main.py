from LinkedList import LinkedList


if __name__ == '__main__':
    print("Linked List")

    my_linked_list = LinkedList()
    my_linked_list.add_head(3)
    my_linked_list.add_head(5)
    my_linked_list.add_at(6, 1)
    my_linked_list.add_tail(0)

    my_linked_list.remove(6)

    my_linked_list.print_list()
