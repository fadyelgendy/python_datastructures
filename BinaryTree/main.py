from Node import Node
from collections import deque

# Depth first Traverse, Iterativly
def df_traverse_iterative(root):
    visited = [root]

    while len(visited) != 0:
        current = visited.pop()

        print(f'{current.data} ', end='')

        if current.right is not None:
            visited.append(current.right)
        
        if current.left is not None:
            visited.append(current.left)
    
    print()

# Depth first traverse, Recursivly
def df_traverse_recursive(root):
    if root is None:
        return
    
    print(f'{root.data} ', end='')

    df_traverse_recursive(root.left)
    df_traverse_recursive(root.right)

# Breadth first traverse, Iterativly
def bf_traverse_iterative(root):
    visited = deque([root])

    while len(visited) != 0:
        current = visited.popleft()

        print(f'{current.data} ', end='')

        if current.left is not None:
            visited.append(current.left)
        
        if current.right is not None:
            visited.append(current.right)
    
    print()

if __name__ == '__main__':
    a = Node('A')
    b = Node('B')
    c = Node('C')
    d = Node('D')
    e = Node('E')
    f = Node('F')

    # Creating tree Manually
    a.left = b
    a.right = c
    b.left = d
    b.right = e
    c.right = f

    #      A
    #    /   \
    #   B     C
    #  / \     \
    # D   E     F

    # Depth first traverse
    df_traverse_iterative(a) # A B D E C F
    df_traverse_recursive(a) # A B D E C F
    print()

    # Breadth first traverse
    bf_traverse_iterative(a) # A B C D E F
