from Stack import Stack

if __name__ == "__main__":
    print("Stack")

    my_stack = Stack()
    print(f'Empty: {my_stack.is_empty()}') # True
    print(f'Size: {my_stack.size()}') # 0

    my_stack.push(1)
    my_stack.push(2)

    print(f'Empty: {my_stack.is_empty()}') # False
    print(f'Peek: {my_stack.peek()}') # [2]
    print(f'Size: {my_stack.size()}') # 2

    print(f'Poped: {my_stack.pop()}') # 2

    print(f'Peek: {my_stack.peek()}') # 1
    print(f'Size: {my_stack.size()}') # 1

    print(f'Poped: {my_stack.pop()}') # 1

    print(f'Peek: {my_stack.peek()}') # -1
    print(f'Size: {my_stack.size()}') # 0