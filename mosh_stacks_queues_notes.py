"""
Mosh's Python Course -- Notes on Stacks

To make a stack in Python you just use the deque...
the double-ended queue.

If you use list operations to implement, it can
take O(n) to do the operations of append or pop. No good.
For this reason you use the deque library, so that pop()
and peek take O(1).

"""

from collections import deque

stack = deque()

stack.append(60)
stack.append(70)
stack.append(80)

while stack:
    print(stack.pop())


""""
All of these are technically deque operations. Know the deque well.

stack([x, y, z])           start a new stack, iterable arg
mystack = dequeue[list]    wrap a list in a deque object
stack.pop()                pops from right side
stack[-1]                  peek -- access rightmost element
stack.popleft()            pops from left side
stack.append(x)            append x right side  
stack.appendleft(x)        append to left side
stack.index(val, l, r)     search for value from index l to index r
stack.remove(val)          remove first instance of value
stack.count(val)           count number of instances of value
stack.insert(val, i)       insert value at index i
stack.reverse()            reverse order of elements
stack.extend([x, y, z])    extend deque to right, iterable arg
stack.extendleft([x, y, z])extend deque to left, iterable arg
stack.clear()              clear out deque



Mosh's DS Course -- Section on Stacks

A stack is literally just like a stack of books. You can only peek at,
or remove, the book on top. It works on the LIFO principle. 

Stack operations, Python deque equivalent, and complexity.

push(x)     stack.append(x)        O(1)
pop()       stack.pop()            O(1)
peek()      inspect stack[-1]      O(1)
isempty()   if stack:  #notempty   O(1)
              --blah
            else:      #empty
              --blah

Stacks don't really work well for lookups.
"""

# Sample Questions 
# Q1. Implement a reverse string method using a stack. 
# Q2. Implement a method that checks if a string's brackets e.g
#     <> () [] are balanced.
# Q3. Design a stack that supports push, pop, and findMin in O(1) time.

# Q1. Implement a reverse string method using a stack. 
def reverseString(string:str) -> str:

    myStack = deque()    
    for i in range(len(string)):
        myStack.append(string[i])
    result = ""
    while myStack:
        result = result + myStack.pop()
    return result

# Q2. Implement a method that checks if a string's brackets e.g
def bracketsAreBalanced(string: str) -> bool:

    myStack = deque()
    for i in range(len(string)):
        if string[i] == '<':
            myStack.append(string[i])
        elif string[i] == '>':
            try:
                myStack.remove('<')
            except:
                return False
        if string[i] == '(':
            myStack.append(string[i])
        elif string[i] == ')':
            try:
                myStack.remove('(')
            except:
                return False
        if string[i] == '[':
            myStack.append(string[i])
        elif string[i] == ']':
            try:
                myStack.remove('[')
            except:
                return False

    if myStack:
        return False
    else:
        return True

# Q3. Design a stack that supports push, pop, and findMin in O(1) time.
def minStack(nums: []) -> int:
    myStack = deque()

    for ele in nums:
        if not myStack: # Add element to top if stack is empty.
            myStack.append(ele)
        elif ele < myStack[-1] or ele == myStack[-1]: # Add element to top if it's min.
            myStack.append(ele)
        else:   # Otherwise, find and settle it in into its proper place in the stack.
            temp = deque()
            while myStack and ele > myStack[-1]:
                temp.append(myStack.pop())
            myStack.append(ele)
            while temp:
                myStack.append(temp.pop())
    print(myStack)  # Print resulting stack. stack[-1] should be min.

print(reverseString("murse"))
print(bracketsAreBalanced("<[[<(1 + 2)]>>"))
minStack([3, 10, 6, 1, 13, 69])
minStack([3, 10, 6, 1, 13, 69])
minStack([3323, 120, 16, 10, 113, 649])


"""
Mosh's DS Course - Queues

Pretty sure you'll just use the deque data structure
from the Collections Python library.

Queues work in FIFO. First-in-first-out. It's like a line
at the DMV.

Stacks are like a stack of books, LIFO, last-in-first-out.

Queues are used for resource-sharing, e.g. printers, processes
in operating systems.

Operations, time complexity, and Python Deque equivalents
  
enqueue   O(1)  deque.append(x)
dequeue   O(1)  deque.popleft(x)
peek      O(1)  deque[0]
isEmpty   O(1)  if deque: 
isFull    O(1)  

"""

# Sample Questions 
# Q1) Reverse a queue using only add, remove, and isEmpty methods. 
# Q2) Implement a queue using an array, arrayQueue, with typical
#     queue operations: enqueue, dequeue, peek, isEmpty, isFull.

# Q1) Reverse a queue using only add, remove, and isEmpty methods. 
def reverseQueue(queue):
    newQueue = deque()
    while queue:
        newQueue.appendleft(queue.popleft())
    return newQueue

myQueueA = deque([1, 3, 5, 9, 12, 25])
print(reverseQueue(myQueueA))

# Q2) Implement a queue using an array, arrayQueue, with typical
#     queue operations: enqueue, dequeue, peek, isEmpty, isFull.
class arrayQueue:
    arr = []    # An array will hold items
    front = []  # Pointer to front of queue
    back = -1   # Pointer to back of queue

    # Init method or constructor will initialize the object
    def __init__(self, array):
        self.front = 0
        self.back = len(array) - 1
        self.arr = array
        print("initialized arrayqueue")
    # Enqueue will add an item to the end of the queue
    def enqueue(self, item):
        self.arr.append(item)
        self.back+=1
        print("added to arrayqueue")
    # Dequeue will return the item at the front of the queue and "remove" it
    def dequeue(self):
        item = self.arr[self.front]
        self.front+=1
        return item
    # Peek will return the item at the front of the list, but not "remove" it
    def peek(self):
        return self.arr[self.front]
        

testArrayQueue = arrayQueue([1, 2, 3, 5])
testArrayQueue.enqueue(69)
print(testArrayQueue.dequeue())
print(testArrayQueue.dequeue())
print(testArrayQueue.peek())

    
