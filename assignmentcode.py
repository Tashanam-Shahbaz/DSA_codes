from singlylinkedlist import *
from doublylinkedlist import *


# 1.	Write an algorithm del_x(H, x) that accepts head pointer H
# to a linked list and deletes all nodes having x in the info field.

def del_x(H, x):
    # see if any initial nodes contain x
    while H is not None and H.data == x:
        H = H.next
    # see if there IS a list left
    if H is None:
        return H
    a = H
    b = a.next
    while b is not None:
        if b.data == x:
            a.next = b.next
            b = a.next
        else:
            a = a.next
            b = b.next

    return H


# o=del_x(o,3)
# o.traverse()
# # O(n)

def del_x2(H, x):
    if H is None:
        return H
    [res, before, xpos] = H.search(x)
    while res:
        if before is None:
            H = H.next
        else:
            before.next = xpos.next
        if H is not None:
            [res, before, xpos] = H.search(x)
        else:
            res = False
    return H


# 2.	Write an algorithm count_x(H, x) that accepts head pointer H
# to a linked list and returns the count of nodes having x in the info field.

def count_x(H, x):
    # see if a list exists
    if H is None:
        return 0
    c = 0
    a = H
    while a is not None:  # i mistakenly wrote a.next here
        if a.data == x:
            c += 1
        a = a.next
    return c


# O(n)

def count_x2(H, x):
    # see if a list exists
    if H is None:
        return 0
    c = 0
    [res, before, xpos] = H.search(x)
    while res:
        c += 1
        start = xpos.next
        if start is not None:
            [res, before, xpos] = start.search(x)
        else:
            res = False
    return c


# 3.	Write an algorithm del_tail(H) that accepts head pointer H
# to a linked list and removes its tail node.

def del_tail(H):
    if H is None or H.next is None:
        return None
    a = H
    b = H.next
    while b.next is not None:
        a = a.next
        b = b.next
    a.next = None
    return H


# O(n)

# 4.	Let L1 and L2 be head pointers to two separate linked lists.
# Write an algorithm combine(L1, L2) to combine them into one list.

def combine(L1, L2):
    if L1 is None:
        return L2
    if L2 is None:
        return L1
    a = L1
    while a.next is not None:
        a = a.next
    a.next = L2
    return L1


# O(n) where n is number of elements in the first list

# 5.	Write an algorithm to traverse a list of integers and split it into two
# sub-lists as soon as a negative integer is encountered in the info field.
# That is, the first node with negative integer in the info field must be
# the last (tail) node in the first sub-list.

def splitonneg(a):
    if a is None:  # no list
        return [None, None]
    # there is atleast one node
    q = a
    while q is not None:
        if q.data < 0:
            p = q.next
            q.next = None
            return [a, p]
        q = q.next
    return [a, None]


# O(n)

# 6.	Write an algorithm insB4tail(H, x) that accepts head pointer H
# to a linked list and inserts a node having info = x before the tail node.

def insB4tail(H, x):
    new = ListNode(x)
    if H is None:
        return new
    if H.next is None:
        new.next = H
        return new
    a = H
    b = H.next
    while b.next is not None:
        a = a.next
        b = b.next
    new.next = b
    a.next = new
    return H


# O(n)

# 7.	Write an algorithm newHead(H, x) that accepts head pointer H
# to a linked list and makes the node having info = x as the new head
# node and deletes all of its predecessor nodes.

def newHead(H, x):
    while H is not None and H.data != x:
        H = H.next
    return H


# O(n)

def newHead2(H, x):
    [res, before, xpos] = H.search(x)
    if res == True:
        return xpos
    return None


# 8.   Write an algorithm insInDlist(H, y, x) that accepts head pointer H
# to a doubly-linked list and inserts a node having info = x after the node with info = y.

def insInDlist(H, y, x):
    ypos = H.search(y)
    if ypos is not None:
        ypos.insertright(x)


# O(n)

# 9.   Write an algorithm MaxDlist(H) that accepts head pointer H
# to a doubly-linked list of real numbers and returns the largest number in the list.

def MaxDlist(H):
    if H is None:
        return None
    max = H.data
    b = H.right
    # check the nodes on the right
    while b is not None:
        if b.data > max:
            max = b.data
        b = b.right
    # check the nodes on the left
    b = H.left
    while b is not None:
        if b.data > max:
            max = b.data
        b = b.left
    return max


# O(n)

# 10.	Write an algorithm insClist(H, y, x) that accepts head pointer H to a circular singly-linked list
# and inserts a node having info = x after the node with info = y without using converting to a linear list.
def insClist(H, y, x):
    if H is None:
        return
    if H is H.next:
        if H.data == y:
            new = ListNode(x)
            new.next = H
            H.next = new
        return
    a = H.next
    while a.data != y and a is not H:
        a = a.next
    if a.data == y:
        new = ListNode(x)
        new.next = a.next
        a.next = new
    return


# O(n)

obj = ListNode(3)
for i in range(5):
    obj.insert(i + 2)
obj.traverse()
obj.circularize()
obj.traverse_circular()
insClist(obj,4,123)
obj.traverse_circular()
