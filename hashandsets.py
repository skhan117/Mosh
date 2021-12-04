"""
Hash

Reviewing from Mosh's Python class on Dictionaries

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
   print(point["a"])       Avoid errors by prefacing with if and in
print(point.get("y"))      Get method gets the value.
                           If key isn't in dictionary, results in None.
point.get("y", 69)         Default return value is 69 if key not in dict.
del point("y")             Delete a key-value pair.
point['tt'] = 21           Add key-value pair.
point[50] = None           Add a key with null value
point[None] = 40           Add a null key with a value. Nulls are fine!
for key in point:          Loop over a dictionary.
   print(key, point[key])  Print key and value.
for x in point.items():    Loop over dict and get key-val pairs as tuples.
   print x
for key, val in point.items():
   print(key, val)         Loop over dict and unpack key-val tuples.

Continuing now with Mosh's class..

HashTables in Java are HashMaps, in JavaScript they're Objects, in Python
they're Dictionaries, in C# they're Dictionaries.

Use them for Key-Value pairs. Like key = employeeNumber, value = Name

employeeNumber enters HashFunction to generate a memoryaddress, which is
where the employeeName will be stored.

The HashFunction is deterministic: anytime you give it X input, it'll give
you Y output. This is why you use it for both storage and retrieval.
HashTable ultimately uses an array to store its objects.

Time Complexity

Insert   O(1)
Lookup   O(1)
Delete   O(1)

You don't have to iterate over everything for your operations! Everything
is going to be very quick. 




Sets

Reviewing from Mosh's Python class on Sets

A set is a collection of items with no duplicates. Use curly braces.
They are unordered collections, so there's no way to access them using
an index. No indexing with sets! Set is implemented as a hash table so
lookups are O(1).

newSet = set()            Make an empty set
nums = [1, 1, 2, 2, 4, 5]
uniques = set(nums)

uniques will now give {1, 2, 4, 5}

uniques.add(7)            Standard methods for adding, removing, etc.
uniques.remove(1) 
len(uniques)

Sets can do a union operation to give items in either set.

first = {1, 2, 3, 5}
second = {1, 4}
result = (first | second)   Union is just single bar, meaning "or".

Sets can also do intersections to give items in both sets.

result = (first & second)   Intersection is &, meaning "and".

You can also get the difference between the two sets. 

result = (first - second)   Difference is -

You can also get symmetri difference -- items in one set or othe other,
but not both.

result = (first ^ second)   Symmetric is ^

You can also check if items are in a set.

if 2 in result:
    print("Yes")

Other set operations are clear(), isdisjoint()

setA.clear()                    This will clear set A
setA.pop()                      Return and remove a random element from set.
setA.isdisjoint(setB)           True if set A shares no items with set B.
                                

Hash Functions

A hash table maps a key to an index value in an array. A hash function takes a
value and maps it to a hash value... or it "hashes." A hash function maps a key
value to an index value. Eg. map 123456 to "Mosh".

Given an array of size X, let's say 100 here, we need to map 123456 to an index
in the array. To do so in a simple way we use a modulus operator. 

In python we can use the hash() method to hash a key to some hash value.

A collision happens when two distinct keys generate the same hash value. 

One way to resolve collisions is to store your hash values in a linkedlist. Instead
of directly adding a hash value to an array, you store it in a linkedlist that
resides at that array index. If you have a collision, you just add the hash value
as a new node placed on that linkedlist. This is called "chaining."

Another way to resolve collisions is to find another address to store a hash value
when a collision occurs. This is called "open addressing." So instead of storing
a key at index 9, you do so at 10.

Re: Chaining. Say you have an array of 5 buckets, or slots. Given a key-value pair
you want to hash the key to find a bucket to store the value. 


"""

# Sample Questions
# Q1. Write a method that finds the first repeating char in a string.
# Q2. Write a method that finds the first nonrepeating char in a string.
# Q3. Write a simple hash function that maps an integer to an index in
#     an array of some given size. 
# Q4. Write a simple hash function that maps a string to an index in an
#     array of some given size.


# Q1. Write a method that finds the first repeated char in a string.
def firstRepeatedCharacter(s:str):
    letters = set() # Start with an empty set.
    for char in s:
        if char not in letters:
            letters.add(char)
        else:
            return char

# Q2. Write a method that finds the first nonrepeating char in a string.
def nonrepeatedChar(s:str):
    letters = {}    # Start with an empty dict.
    for char in s:
        if char not in letters:
            letters[char] = 1
        else:
            val = letters.get(char) + 1
            letters[char] = val
            
    for char in s:
        if letters.get(char) == 1:
            return char

# Q3. Write a simple hash function that hashes an integer to some index value.
def simpleHash(num:int, size:int):
    return num % size

# Q4. Write a simple hash function that hashes a string to some index value.
def simpleHashString(s:str, size:int):
    x = 0
    for letter in s:
        x = x + ord(letter)   # We use the ord() function to get ascii code for char.
    return x % size
    



print(firstRepeatedCharacter("My Green Mile"))
print(nonrepeatedChar("My Green Mile"))
print(simpleHash(69, 10))

print(simpleHashString("abcdef", 10))
