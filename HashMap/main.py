from HashMap import HashMap

if __name__ == '__main__':
    myHashMap = HashMap()
    
    myHashMap.add(40, 900)
    myHashMap.add(6, 28)
    myHashMap.add(4, 65)
    myHashMap.add(9, 78)

    myHashMap.add(1, 5)
    print(f'Get[1]: {myHashMap.get(1)}')

    myHashMap.add(1, 6)
    print(f'Get[1]: {myHashMap.get(1)}')

    print(f'Get[500]: {myHashMap.get(500)}')
    myHashMap.print_hash_map()

    print(f'Remove[40]: {myHashMap.remove(40)}')
    myHashMap.print_hash_map()