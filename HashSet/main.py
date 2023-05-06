from HashSet import HashSet

if __name__ == '__main__':
    myHashSet = HashSet()

    myHashSet.add(1, 400)
    myHashSet.add(2, 500)
    myHashSet.add(2, 250)
    myHashSet.add(600, 456)

    myHashSet.print_hash_set()

    print(f'Contains[4]: {myHashSet.contains(4)}')
    print(f'Contains[600]: {myHashSet.contains(600)}')
    print(f'Remove[2]: {myHashSet.remove(2)}')
    print(f'Remove[4]: {myHashSet.remove(4)}')

    print(f'Get[600]: {myHashSet.get(600)}')
