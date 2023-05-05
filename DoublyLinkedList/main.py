from DoublyLinkedList import DoublyLinkedList

if __name__ == '__main__':
    myDBL = DoublyLinkedList()

    print(f'Size: {myDBL.get_size()}')

    myDBL.add_head(1)
    myDBL.add_head(0)
    myDBL.add_tail(2)
    myDBL.add_tail(3)

    myDBL.add_at(0, 300)
    myDBL.add_at(3, 500)

    myDBL.print_list()
    myDBL.print_list_reverse()
    print(f'Size: {myDBL.get_size()}')

    print(f'[{myDBL.remove(500)}] removed!')
    print(f'[{myDBL.remove(300)}] removed!')
    print(f'[{myDBL.remove(0)}] removed!')
    print(f'[{myDBL.remove(3)}] removed!')

    myDBL.print_list()
    print(f'Size: {myDBL.get_size()}')
