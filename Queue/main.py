from Queue import Queue

if __name__ == '__main__':
    myQueue = Queue()

    print(f'Empty: {myQueue.is_empty()}') # True
    print(f'Size: {myQueue.size()}') # 0
    print(f'Peek: {myQueue.peek()}') # -1

    myQueue.enqueue(1) # [1]
    myQueue.enqueue(2) # [2, 1]
    myQueue.enqueue(3) # [3, 2, 1]

    print(f'Empty: {myQueue.is_empty()}') # False
    print(f'Size: {myQueue.size()}') # 3
    print(f'Peek: {myQueue.peek()}') # 1

    print(f'Dequeued: {myQueue.dequeue()}') # 1
    print(f'Dequeued: {myQueue.dequeue()}') # 2
    print(f'Dequeued: {myQueue.dequeue()}') # 3
    print(f'Dequeued: {myQueue.dequeue()}') # -1

    print(f'Empty: {myQueue.is_empty()}') # True
    print(f'Size: {myQueue.size()}') # 0
    print(f'Peek: {myQueue.peek()}') # -1