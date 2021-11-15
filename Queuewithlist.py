from singlylinkedlist import ListNode


class queue:
    def __init__(self):
        self.element = list()

    def __len__(self):
        return len(self.element)

    def isEmpty(self):
        return len(self) == 0

    def enqueue(self, item):
        self.element.append(item)

    def dequeue(self):
        assert not self.isEmpty(), "Empty lIST"
        self.pop(0)

    def traverse(self):
        print("Treversing...")
        for i in range(len(self.element)):
            print(self.element[i], end=" ")
        print()


# myobj=queue()
# myobj.enqueue(12)
# for i in range(5):
#     myobj.enqueue(i+2)
# myobj.traverse()
# print(myobj.isEmpty())

# myobj.traverse()
class Node_queue:
    def __init__(self):
        self.front = None
        self.rare = None

    def __len__(self):
        return len(self.front)

    def isEmpty(self):
        return len(self.front) == 0




    def enqueue(self, item):
        new = ListNode(item)
        if self.front == None:
            self.front = new
            self.rare = self.front
        else:
            self.rare.insert(item)
            self.rare = self.rare.next

    def traverse(self):
        assert not self.isEmpty(), "Empty lIST lenght 0"
        # a = self.front
        # while a is not None:
        #     print(a.data, end=" ")
        #     a = a.next
        if self.front is not None:
            self.front.traverse()
        print()

    def dequeue(self):
        assert not self.isEmpty(), "Empty lIST"
        a = self.front.data
        self.front = self.front.next
        return a


my_obj=Node_queue()
my_obj.enqueue(23)
my_obj.enqueue(99)
my_obj.traverse()
for i in range(5):
    my_obj.enqueue(i+2)

my_obj.traverse()
my_obj.dequeue()
my_obj.traverse()

# class priority_queue:
#     def __init__(self):
#         self.q = list()
#
#     def __len__(self):
#         return len(self.q)
#
#     def isEmpty(self):
#         return len(self.q) == 0
#
#     def lowest(self):
#         if not self.isEmpty():
#             return self.q[0][0]
#
#     def highest(self):
#         if not self.isEmpty():
#             return self.q[-1][0]
#
#     def enqueue(self, pri, item):
#         new = [pri, item]
#
#         if self.isEmpty():
#             self.q.append(new)
#             return
#         if pri >= self.highest():
#             self.q.append(new)
#             return
#         if pri < self.lowest():
#             self.q.insert(0, new)
#             return
#         for i in range(1, len(self)):
#             if pri < self.q[i][0]:
#                 self.q.insert(i, new)
#                 return
#
#     def dequeue(self):
#         assert not self.isEmpty()
#         self.q.pop(0)
#
#     def traverse(self):
#         if not self.isEmpty():
#             for i in range(len(self)):
#                 print(self.q[i], end=" ")
#             print()
#
#
# o = priority_queue()
# o.traverse()
# o.enqueue(2,"C")
# o.enqueue(0,"A")
# o.enqueue(1,"B")
# o.enqueue(5,"E")
# o.traverse()
#
