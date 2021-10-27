"""
Mosh LinkedList Notes

A LinkedList is a series of nodes. Each node contains
a piece of data, and a reference to the next node.

The first node is called the 'head' and the last is called
the 'tail'.

Lookup is O(n), since you have to check each node for a value.

Index is O(n), since you have to traverse the whole list for a
specific item.

Insertion at the end of an LL is O(1) since you're just adding a
new node,then adding two pointers to it -- one from previous last
node, one from 'tail'.

Insertion at the beginning is O(1) since you're just pointing
'head' to it then having the new node point to the previoushead.

Deleting from the beginning of an LL takes O(1), since you're
just pointing 'head' to the second node of the LL.

Deleting from the middle of an LL takes O(n), since you have to
traverse the LL to find the value to delete, the set up the
pointers again.

Deleting from the end of an LL takes O(n), since you have to find
the second-to-last node in the LL, point 'tail' to it, then point
this node to a null value. 

Make sure to use the updated notation for function parameters and
returns. 

Review Questions:
1) Write a Node class.
2) Write a LinkedList class.
3) Add an addFirst method.
4) Add an addLast method.
5) Add a deleteFirst method.
6) Add a deleteLast method.
7) Add a contains method.
8) Add an indexOf method.
9) Add a reverse method.
10. Add a kth from the end method.
11. Check if linked list is a palindrome.
12. Rotate list by k places.


"""

# 1. Write a Node class.
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

# 2. Write a LinkedList class.
class LinkedList:
    def __init__(self, value):
        self.head = Node(value)
        self.tail = self.head
    def print(self):
        a = self.head
        while (a.value is not None):
            print(a.value)
            if a.next is not None:
                a = a.next
            else:
                return
        
    # 3. Add an addFirst method.
    def addFirst(self, newValue: int):
        newNode = Node(newValue)
        newNode.next = self.head
        self.head = newNode

    # 4. Add an addLast method.
    def addLast(self, newValue: int):
        newNode = Node(newValue)
        self.tail.next = newNode
        self.tail = newNode

    # 5. Add a deleteFirst method.
    def deleteFirst(self):
        self.head = self.head.next

    # 6. Add a deleteLast method.
    def deleteLast(self):
        a = self.head
        while a.next is not self.tail:
            a = a.next
        a.next = None
        self.tail = a

    # 7. Add a contains method
    def contains(self, findValue: int) -> bool:
        a = self.head
        while a.value is not findValue:
            a = a.next
            if a.next is None:
                return False
        return True
            
    # 8. Add an indexOf method.
    def indexOf(self, findValue: int) -> int:
        a = self.head
        index = 0
        while a.value is not findValue:
            if a is self.tail:
                return -1
            a = a.next
            index+=1
        return index
    # 9. Add a reverse method.
    def reverse(self):
        a = None
        b = self.head
        while b is not None:
            c = b.next
            b.next = a
            a = b
            b = c
        self.tail = self.head
        self.head = a
    # 10. Add a kth from the end method.
    def kthFromEnd(self, k):
        a = self.head
        b = self.head
        while k != 0:
            b = b.next
            k-=1
        while b is not self.tail:
            a = a.next
            b = b.next
        return a.value
    # 11. Check if linked list is a palindrome.
    def isPalindrome(self) -> bool:
        a = self.head
        stack = []
        while a is not None:
            stack.append(a.value)
            a = a.next
        b = self.head
        while b.next is not None:
            check = stack.pop()
            if b.value != check:
                return False
            else:
                b = b.next
        return True
    # 12. Rotate list by k places.
    def rotate(self, k: int):
        size = 1
        a = self.head
        while a.next is not None:
            a = a.next
            size+=1
        print("size is", size)
        newHeadIndex = size - k
        newTailIndex = size - k - 1
        b = self.head
        for i in range(newTailIndex):
            b = b.next
        print("new tail is", b.value)    
        c = b.next
        print("new head is", c.value)
        a.next = self.head
        b.next = None
        self.head = c




# Tester
firstLL = LinkedList(50)
firstLL.print()
firstLL.addFirst(51)
firstLL.print()
firstLL.addLast(69)
firstLL.print()
firstLL.addLast(214)
firstLL.addLast(124)
firstLL.addLast(9)
firstLL.addLast(99)
firstLL.print()
firstLL.deleteFirst()
firstLL.print()
firstLL.deleteLast()
firstLL.print()
print(firstLL.contains(420))
print(firstLL.contains(69))
firstLL.print()
print(firstLL.indexOf(9))
print(firstLL.indexOf(50))
print(firstLL.indexOf(124))
firstLL.reverse()
firstLL.print()
firstLL.addLast(122)
firstLL.addLast(125)
print("Printing list")
firstLL.print()
print(firstLL.kthFromEnd(3))
print(firstLL.isPalindrome())
secondLL = LinkedList(12)
secondLL.addFirst(420)
secondLL.addLast(420)
print(secondLL.isPalindrome())
print("Printing list")
firstLL.print()
firstLL.rotate(4)
print("first rotation of 4")
firstLL.print()
print("second rotation of 1")
firstLL.rotate(1)
firstLL.print()

