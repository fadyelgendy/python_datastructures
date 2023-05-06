from HashSet import HashSet

if __name__ == '__main__':
    myHashSet = HashSet()

    myHashSet.add(1)
    myHashSet.add(2)
    myHashSet.add(2)

    print(f'Contains[4]: {myHashSet.contains(4)}')
    print(f'Remove[2]: {myHashSet.remove(2)}')
    print(f'Remove[4]: {myHashSet.remove(4)}')

    print(f'Get: {myHashSet.get(1)}')

    myHashSet.print_hash_set()