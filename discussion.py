"""
PART 1: DISCUSSION QUESTIONS

RECURSION

1.  Recursion is a function that calls itself. When it reaches the Base Case, it returns a value, but it needs to return previous functions and close them. This is like Russian nesting dolls that open but need to close each one when it goes back.

2.  It is necessary to have a Base Case to know when recursion is done. If there is no Base Case, a Runtime Error will occur.


GRAPHS

1.  A Graph is like a Tree, except it can contain loops ("cycles") and the relationships can be directed or non-directed.

2.  A Graph is different from a Tree because a Graph does not have hierarchy, but a Tree does.

3.  An example of something that would be good to model with a Graph is users who are friends with other users, like Facebook.


PERFORMANCE OF DIFFERENT DATA STRUCTURES

Data Structure                  Index   Search  Add-R   Add-L   Pop-L   Pop-R
Python List (Array)             O(1)    O(n)    O(1)    O(n)    O(n)    O(1)
Linked List                     O(n)    O(n)    O(1)    O(1)    O(1)    O(n)
Doubly-Linked List              O(n)    O(n)    O(1)    O(1)    O(1)    O(1)
Queue (as Array)                X       X       O(1)    X       O(n)    X
Queue (as LL or DLL)            X       X       O(1)    X       O(1)    X
Stack (as Array, LL, or DLL)    X       X       O(1)    X       X       O(1)**
Deque (as DLL)                  X       X       O(1)    O(1)    O(1)    O(1)


**  Stack - Pop-R
    I originally put down O(n) due to Linked List being O(n) for Pop-R.
    But the trick for using LL is to keep the stack reversed, so you can push onto the head and pop off from the head, rather than the tail, and this way both push and pop can be O(1) operations for a singly-linked list.


Data Structure          Get         Add     Delete  Iterate Memory
Dictionary (Hash Map)   O(1)        O(1)    O(1)    O(n)    medium
Set (Hash Map)          O(1)        O(1)    O(1)    O(n)    medium
Binary Search Tree      O(log n)    O(n)    O(n)    O(1)    a little
Tree                    O(n)        O(1)    O(1)    O(1)    a little



"""