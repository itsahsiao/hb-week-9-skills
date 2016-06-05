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


SORTING

1.  Bubble Sort starts from the beginning of the list, and compares the first two numbers to see which number is the larger of the pair, swapping them (if needed) to have the bigger number on the right. It keeps doing this until the largest number in the list is on the very right (end of list). This is only the first iteration of the list, so it goes through the same process to have the second largest number being second from the right, until all numbers are sorted from smallest to largest.

    The list is always kept in place for Bubble Sort, so runspace is O(1).

    Runtime for Bubble Sort is O(n^2).

2.  Merge Sort uses recursion, diving the list into a list of one. It then compares the first element of both lists to see which number is smaller and pops the smaller number into a new list, the results list. Once one of the lists is empty, then the number(s) in the other list gets popped and appended to the results list. The results list will have the numbers sorted from smallest to largest. As recursion is called, it has to return this and close the function, returning to the previous function and doing the same thing, until finally, it gets to the original function and returns the results list with all numbers sorted.

    As a new list is created each time, runspace is O(n).

    Runtime for Merge Sort is O(n log n).

3.  Quick Sort uses a pivot, chosen randomly, from the list, and moves all numbers lower than the pivot to the left of the pivot (the beginning of the list). and all numbers bigger than the pivot to the right of the pivot (the end of the list). The pivot is then in the right place, and the same process executes on the two halves (recursion), where the first half of the list will have a random pivot to arrange the numbers according and set the pivot in the right place. It keeps doing this with pivots and partioning until all numbers are sorted from smallest to largest.

    As the list is in place, run space is O(1).

    Runtime for Quick Sort is O(n log n).


GIT BRANCHING

1.  An instance when you would use git branching is when you want to test out an idea that would not affect the main branch.

2.  A pull request is a Github-specific feature where you can ask project owners to check out your branch and see if they would merge it into another branch. This is how you contribute code on Github.

"""