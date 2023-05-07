from Node import Node
from collections import deque

# Depth first Traverse, Iterativly
def df_traverse_iterative(root):
    if root is None:
        return

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
    if root is None:
        return

    visited = deque([root])

    while len(visited) != 0:
        current = visited.popleft()

        print(f'{current.data} ', end='')

        if current.left is not None:
            visited.append(current.left)

        if current.right is not None:
            visited.append(current.right)

    print()


# Contains Iterative
def contains_iterative(root, val):
    if root is None:
        print(f'[{val}] in tree: False')
        return

    visited = deque([root])

    while len(visited) != 0:
        current = visited.popleft()

        if current.data == val:
            print(f'[{val}] in tree: True')
            return

        if current.left is not None:
            visited.append(current.left)

        if current.right is not None:
            visited.append(current.right)

    print(f'[{val}] in tree: False')
    return


# Contains, recursively
def contains_recursive(root, val):
    if root is None:
        return False

    if root.data == val:
        return True

    return contains_recursive(root.left, val) or contains_recursive(root.right, val)


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
    df_traverse_iterative(a)  # A B D E C F
    df_traverse_recursive(a)  # A B D E C F
    print()

    # Breadth first traverse
    bf_traverse_iterative(a)  # A B C D E F

    # Contains iterative
    contains_iterative(a, 'E')  # true
    contains_iterative(a, 'X')  # false

    # Contains, recursively
    print(f'{contains_recursive(a, "D")}') # True
    print(f'{contains_recursive(a, "G")}') # False
