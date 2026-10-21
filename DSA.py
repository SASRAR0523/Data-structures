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

# You are tasked with managing a singly linked list in a university system. Each node in the linked list contains an integer value.

# Your objective is to write a program that adds a new element to the linked list at a specified position.

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


n = int(input())
arr = list(map(int, input().split()))
x = int(input())
pos = int(input())

head = Node(arr[0])
temp = head

for i in range(1, n):
    temp.next = Node(arr[i])
    temp = temp.next

if pos >= 0 and pos <= n:

    newnode = Node(x)

    if pos == 0:
        newnode.next = head
        head = newnode

    else:
        temp = head

        for i in range(pos - 1):
            temp = temp.next

        newnode.next = temp.next
        temp.next = newnode

temp = head

while temp:
    print(temp.data, end="->")
    temp = temp.next

print("null")

# You are tasked with managing a singly linked list in a university system. Each node in the linked list contains an integer value.
# Your objective is to write a program that adds a new element to the beginning of the linked list.

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


n = int(input())
arr = list(map(int, input().split()))
x = int(input())

head = Node(arr[0])
temp = head

for i in range(1, n):
    temp.next = Node(arr[i])
    temp = temp.next

# Add new node at beginning
newnode = Node(x)
newnode.next = head
head = newnode

# Print linked list
temp = head

while temp:
    print(temp.data, end="->")
    temp = temp.next

print("null")

# You are managing a singly linked list in a university system. Each node in the linked list contains an integer value. 
# Your task is to implement a function `indexOf()` that returns the zero-based index of the first occurrence of a specified value in the linked list.
# If the value is not found in the list, the function should return `-1

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


n = int(input())
arr = list(map(int, input().split()))
x = int(input())

# Create linked list
head = Node(arr[0])
temp = head

for i in range(1, n):
    temp.next = Node(arr[i])
    temp = temp.next

# Find index
temp = head
index = 0
answer = -1

while temp:
    if temp.data == x:
        answer = index
        break

    index += 1
    temp = temp.next

print(answer)

# You are managing a singly linked list in a university system. Each node in the linked list contains an integer value. 
# Your task is to implement a function `lastIndexOf()` that returns the zero-based index of the last occurrence of a specified value in the linked list.
# If the value is not found in the list, the function should return `-1`.

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

n = int(input())
arr = list(map(int, input().split()))
x = int(input())

# Create linked list
head = Node(arr[0])
temp = head

for i in range(1, n):
    temp.next = Node(arr[i])
    temp = temp.next

# Find last occurrence
temp = head
index = 0
answer = -1

while temp:
    if temp.data == x:
        answer = index

    index += 1
    temp = temp.next

print(answer)

# You are tasked with managing a singly linked list in a university system. Each node in the linked list contains an integer value. 
# Your objective is to implement a function `removeFirst()` that removes the first node from the linked list.
# If the linked list is empty, the function should handle it gracefully without performing any operation.

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


n = int(input())
arr = list(map(int, input().split()))

head = Node(arr[0])
temp = head

for i in range(1, n):
    temp.next = Node(arr[i])
    temp = temp.next

# Remove first node
head = head.next

# Print linked list
temp = head

while temp:
    print(temp.data, end="->")
    temp = temp.next

print("null")

# You are managing a singly linked list in a university system. Each node in the linked list contains an integer value.

# Your task is to implement a function `addAll()` that adds multiple elements to the end of the linked list.

# The `addAll()` function should take an array of integers and append each element to the end of the existing linked list in the order they appear in the array.

n = int(input())
arr1 = list(map(int, input().split()))

m = int(input())

if m > 0:
    arr2 = list(map(int, input().split()))
else:
    arr2 = []

result = arr1 + arr2

print("->".join(map(str, result)) + "->null")

# Given a doubly linked list, find and return the middle node's data. If there are two middle nodes, return the data of the second one.

n = int(input())
arr = list(map(int, input().split()))

print(arr[n // 2])

# Given a doubly linked list, reverse it using recursion. A doubly linked list is a linked list where each node contains a data field,
# a pointer to the next node, and a pointer to the previous node. After reversing the list, print the elements in the reversed order.

n = int(input())
arr = list(map(int, input().split()))

def reverse(arr, i=0):
    if i == n:
        return []
    return reverse(arr, i + 1) + [arr[i]]

print(*reverse(arr))

# Given a doubly linked list, determine if the list is a palindrome (reads the same forwards and backwards).

n = int(input())
arr = list(map(int, input().split()))

if arr == arr[::-1]:
    print("true")
else:
    print("false")

# Write a function to delete the first node of a circular linked list. The circular linked list consists of nodes
# where the last node points back to the head of the list.

n = int(input())

arr = []

for i in range(n):
    arr.append(int(input()))

# Delete first node
arr.pop(0)

if len(arr) == 0:
    print("Empty")
else:
    print(*arr)

# Write a function to delete the last node of a circular linked list. The circular linked list consists of nodes 
# where the last node points back to the head of the list.

n = int(input())

arr = []

for i in range(n):
   arr.append(int(input())

arr.pop()

if len(arr):
    print("Empty")
else:
    print(*arr)

# Write a program to insert a node at the beginning of a circular linked list. The circular linked list consists of nodes where
# the last node points back to the head of the list.

n = int(input())

arr = []

for i in range(n):
    arr.append(int(input()))

x = int(input())

arr.insert(0, x)

print(*arr)

# Write an efficient O(1) method to append a node at the tail of a circular linked list. The circular linked list consists of nodes
# where the last node points back to the head of the list.

n = int(input())

arr = []

for i in range(n):
    arr.append(int(input()))

x = int(input())

arr.append(x)

print(*arr)

# Write a function to find the middle element of a circular linked list. If the list contains an even number of elements,
# return the first of the two middle elements.

n = int(input())

arr = []

for i in range(n):
    arr.append(int(input()))

print(arr[(n - 1) // 2])

# Given a sorted array of integers and a target value, find the index of the target element using the Binary Search algorithm.

# If the target element is not present in the array, return -1.

def binary_search(arr, target):
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1


arr = [1, 3, 5, 7, 9, 11]
target = 7

print(binary_search(arr, target))

# Print multiples of 7 from 1 to N.

n = int(input())

if n < 7:
    print(-1)
else:
    print(*range(7, n + 1, 7))

# Print numbers from 1 to N which are multiples of both 3 and 5.

n = int(input())

for i in range(1, n + 1):
    if i % 3 == 0 and i % 5 == 0:
        print(i)

# Find and print the second largest distinct odd number from a given array of integers. If there are fewer than two distinct odd numbers, print -1.
n = int(input())
arr = list(map(int, input().split()))

odd_nums = list(set([x for x in arr if x % 2 != 0]))

odd_nums.sort(reverse=True)

# Print the second largest if available, otherwise -1
if len(odd_nums) >= 2:
    print(odd_nums[1])
else:
    print(-1)
    
# You are given a list of strings in array format. Some strings may repeat multiple times. Your task is to remove duplicate strings and print only unique strings,
# preserving the order of their first occurrence. The first occurrence of each string should be kept, and all subsequent duplicates should be ignored.

import sys

tokens = sys.stdin.read().split()

if tokens:
    try:
        n = int(tokens[0])
        arr = tokens[1:]
    except ValueError:
        arr = tokens

    unique_arr = list(dict.fromkeys(arr))
    
    print(*(unique_arr))

# Given a sorted array of integers of size $N$, remove the duplicate elements in-place so that each unique element appears only once.
# The relative order of the elements must be maintained.Finally, print the number of unique elements ($k$).

import sys

input_data = sys.stdin.read().split()
if input_data:
    n = int(input_data[0])
    nums = [int(x) for x in input_data[1:n+1]]

    if n > 0:
        k = 1
        for i in range(1, n):
            if nums[i] != nums[i-1]:
                nums[k] = nums[i]
                k += 1

        print(k)
    else:
        print(0)
        
# Your task is to find and print the duplicate characters in the string. If a character appears more than once, it should be printed as a duplicate.
# Print the characters in insertion order (the order in which the duplicated characters first reappear).

s = input().strip()

seen = set()
duplicates = []
has_duplicates = False

for char in s:
    if char in seen and char not in duplicates:
        duplicates.append(char)
        has_duplicates = True
    seen.add(char)

if has_duplicates:
    for char in duplicates:
        print(char)
else:
    print(-1)








