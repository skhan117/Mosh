"""
Notes on Mosh's Python Course, Section 5: Data Structures
These are the data structures built into Python.
"""

"""
--
Lists

Every object in a list can be of a different type. Super useful!

To start a new list just type in square brackets:
list = []
letters = ["a", "b", "c"]

Make a list of lists, a 2D list:
matrix = [[1, 2], [3, 4]]

Make a list of 10 6's:
numbers = [6] * 10

Easily Concatenate lists by using +:
combined = letters + numbers

We can use the range function to easily populate lists.
This will make a list of numbers from 0 to 19:
great = list(range(20))

Strings are iterable in Python. You  can pass a String
to a list to get a list of characters:
chars = list("Hello world")

You can get the length of a list by using the len(list) function:
len(chars) will give 11

You can access each item in the list using a square bracket:
chars[1] will give 'e', which is one from the beginning of the list
chars[-1] will give 'l', which'll return an item from the end of the list

You can slice a list by doing this:
chars[0:3] will yield a new list spanning from index 0 to index 2.
chars[:3] will yield list spanning from beginning to index 2.
chars[3:] will yield list spanning from index 3 to end.
chars[::2] will yield list with every second item.
chars[::3] will yield list with every third item.

nums = list(range(20)) will yield list from 0 to 19
print(nums[::2]) will print every 2nd item
print(nums[::-1]) will print every item in list in reverse order
print(nums[::-2]) will print every 2nd item in list in reverse order

--
List Unpacking

You can do this, but it's tedious.
nums= [1, 2, 3]
first = nums[0]
second = nums[1]
third = nums[2]

Instead you can unpack the list into multiple variables:
nums = [1, 2, 3]
first, second, third = nums

You need to have a variable for each item or else you'll get an error.

You can assign variables to first two items then pack rest in another list.
nums = [1, 2, 3, 4, 5, 6, 7, 8]
first, second, *others = nums

You can use packing in a parameter, then call this function with
any number of arguments. Python will get all the arbitrary arguments
and pack them into a list.

def multiply(*integers)
multiply(1, 2, 3, 4, 5)

You can get the first and last item, then pack the others.
first, *others, last = nums

--
Looping over lists

You can use for loop to loop over a list.
letters = ["a", "b", "c", "d", "e", "f"]

for letter in letters:
    print(letter)

You can use enumerate to access index of each item. Enumerate will
make tuples for each item... here it's (index, letter). This will
print out each item's index and its value.

for letter in enumerate(letters):
    print(letter[0], letter[1)


--
Stacks


LIFO. You use Python's list function. Easy review.
stack = []         Make a new stack.
stack.append(1)    Push onto top of stack.
stack.pop()        Pop from stack.
if not stack:      Check if stack is empty. Will give True if so.
stack[-1]          Access the top item in the stack.

--
Queues

FIFO. You use Python's deque object. If you use list, when you
delete from a first of 1000 items, you have to move remaining 999
over.

from collections import deque

queue = deque([])       Wrap empty list in dequeue object.

queue.append(1)         Append 1.
queue.popleft()         Will pop from left side of dequeue.


--
Tuples

A tuple is a read-only list. You cannot modify it. Use it when you're
working with data that you don't want to accidentally modify.

point = (1, 2)     Here you have x and y coordinates.
point = 1, 2       You don't need parantheses.

point = ()         Define an empty tuple.
point = 1,         1 variable tuple is defined by trailing comma.

point = (1, 2) + (1, 3)  Concatenate two tuples.

point = (1, 3) * 3       Multiplication operator repeats tuples.

letters = tuple("lette") Make tuple of string since it's iterable.


if 10 in point:          Can use in operator.
   print("okay")
      
point(0:2)               Access items at index 0 and 1 in tuple.

--
Swapping variables

Old way:
x = 11
y = 13
z = x
x = y
y = z

New way in Python:
x, y = y,x

Can also just declare variables this way. It's a tuple on the right
that gets unpacked into variables on the left. 
a, b = 13, 10


--
Arrays

For 99% of the cases, lists will work. Arrays are slightly faster though,
especially when dealing with very long lists. It improves performance a bit.
Arrays need to be hard-typed though. I like lists better.

from array import array

nums = array("i", [1, 2, 3, 4, 5])     First argument is typecode, look it up. Second
                                       is the list in question.

nums.append(6)
nums.insert(2, 8)
nums.pop()


--
Sets

A set is a collection of items with no duplicates. Use curly braces.
They are unordered collections, so there's no way to access them using
an index. No indexing with sets! Set is implemented as a hash table so
lookups are O(1).

nums = [1, 1, 2, 2, 4, 5]
uniques = set(nums)

uniques will give {1, 2, 4, 5}

uniques.add(7)            Standard methods for adding, removing, etc.
uniques.remove(1) 
len(uniques)

Sets can do a union operation to give items in either set.

first = {1, 2, 3, 5}
second = {1, 4}

result = (first | second)   Union is just single bar.

Sets can also do intersections to give items in both sets.

result = (first & second)   Intersection is &.

You can also get the difference between the two sets. 

result = (first - second)   Difference is -

You can also get symmetri difference -- items in one set or othe other,
but not both.

result = (first ^ second)   Symmetric is ^

You will check if items are in a set.

if 2 in result:
    print("Yes")


----
Dictionary

Dictionary is a collection of key-value pairs. Example is 
name -> phonenumber. You don't have index. You can only use
key to look up a value. The key must be in immutable types --
so we usually only use integer or string. The value can be
any type.


point = {}
point = {"x":1, "y": 2}    Start a new dictionary.
point = dict(x=1, y=2)     This does the same thing as above.
print(point["y"])          You check value by square brackets.
if "a" in point:           Super-easy lookup
   print(point["a"])       Avoid errors by prefacing with if.. in
print(point.get("y"))      Get method gets the value.
                           If key isn't in dictionary, results in None.
point.get("y", 69)         Default return value is 69 if key not in dict.
del point("y")             Delete a key-value pair.
point['tt'] = 21           Add key-value pair.

for key in point:          Loop over a dictionary.
   print(key, point[key])  Print key and value.

for x in point.items():    Loop over dict and get key-val pairs as tuples.
   print x

for key, val in point.items():
   print(key, val)         Loop over dict and unpack key-val tuples.


---
Dictionary Comprehensions

values = []                Start a list
for x in range(5):         Populate list
   values.append(x * 2)    

values = [x * 2 for x in range(5)]   This line of code replaces stuff above.
List comprehension is as follows:
[expression for item in items]

You can also do "Set Comprehensions"

values = {}
values = {x * 2 for x in range(5)}

A set is a set of values {2, 4, 5, 6} -- each one is unique. No duplicates.

A dictionary is a set of key-value pairs. {2: "ab", 4: "rr", 7: "tt"}



You can also do "Dictionary Comprehensions"

values = {x : x * 5 for x in range(5)}


---
Generator objects

You can save memory by using a generator object instead of a list in a
list comprehension expression.

The below will print out 1000 numbers, but it will take up 1000 bytes
of memory.

values = [x * 3 for x in range(1000)]
for num in values:
   print(num)

Replace it with the below generator expression. It will also print out
1000 numbers, but it will only take up 100 bytes of memory.

values = (x * 3 for x in range(1000)
for num in values:
   print(num)

Each time the generator generates the number from an iterable object
without storing it in memory, as the list does. So you save memory.

However, you can't print its length -- a generator object has no length.
You also can't access it all at once, it needs to be tied to an
iterable. 

"""


