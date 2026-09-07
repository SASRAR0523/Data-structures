# Write a function to find the top element (peek) of a stack. The stack should be implemented using an array. If the stack is empty, the function should return -1.

n = int(input())

stack = []

for i in range(n):
    stack.append(int(input()))

if n == 0:
    print(-1)
else:
    print(stack[-1])

# Write a function to reverse a given string using a stack.

def reverse_string(s):
    stack = []

    for ch in s:
        stack.append(ch)

    result = []

    while stack:
        result.append(stack.pop())

    return ''.join(result)


s = input()
print(reverse_string(s))

# Write a function to check if a given string of parentheses is balanced using stack.

# A string is considered balanced if every opening parenthesis ((, {, [) has a corresponding closing parenthesis (), }, ]) in the correct order.

def is_balanced(s):
    stack = []

    pairs = {
        ')': '(',
        ']': '[',
        '}': '{'
    }

    for ch in s:
        if ch in "([{":
            stack.append(ch)
        else:
            if not stack or stack.pop() != pairs[ch]:
                return False

    return len(stack) == 0


s = input()
print(str(is_balanced(s)).lower())

# You are given an array of integers representing a queue. Your task is to reverse the order of elements in the queue.

def reverse_queue(queue):
    stack = []

# Add queue elements to stack
    for element in queue:
        stack.append(element)

    # Remove elements from stack
    result = []
    while stack:
        result.append(stack.pop())

    return result


n = int(input())

if n == 0:
    print("null")
else:
    queue = list(map(int, input().split()))
    reversed_queue = reverse_queue(queue)
    print(*reversed_queue)

# You are required to implement a queue data structure using a singly linked list. A queue follows the First-In-First-Out (FIFO) principle,
# where the first element added is the first one to be removed. Your task is to simulate the behavior of a queue by utilizing a linked list. 
# The implemented queue should support all the functions of a normal queue: enqueue, dequeue, front, and empty.

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


front = None
rear = None

n = int(input())

for _ in range(n):
    op = input().split()

    if op[0] == "enqueue":
        new = Node(int(op[1]))

        if rear is None:
            front = rear = new
        else:
            rear.next = new
            rear = new

    elif op[0] == "dequeue":
        if front is None:
            print("Error")
        else:
            front = front.next
            if front is None:
                rear = None

    elif op[0] == "front":
        if front is None:
            print("Error")
        else:
            print(front.data)

    elif op[0] == "empty":
        print("true" if front is None else "false")
