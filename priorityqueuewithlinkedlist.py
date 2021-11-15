class Node:
    def __init__(self, pri, item):
        self.pri = pri
        self.data = item
        self.next = None
class priority_queue:
    def __init__(self):
        self.front=None
        self.rear=None

    def __len__(self):
        if self.front is None:
            return 0

        i = 0
        a = self.front
        while a is not None:
            i += 1
        a = a.next
        return i

    def isEmpty(self):
        return self.front is None

    def enqueue(self, pri, item):
        new = Node(pri, item)

        if self.front is None:
            self.front = new
            self.rear = new
            return
        if self.front.pri > pri:
            new.next = self.front
            self.front = new
            return
        if self.rear.pri <= pri:
            self.rear.next = new
            self.rear = new
            return
        x = self.front
        y = x.next
        while y is not None and y.pri <= pri:
            x = x.next
            y = y.next
        x.next = new
        new.next = y
        if y is None:
            self.rear = new

    def dequeue(self):
        assert not self.isEmpty(), "Empty queue!"

        x = self.front.pri
        y = self.front.data
        self.front = self.front.next
        return [x, y]

    def traverse(self):
        if not self.isEmpty():
            a = self.front

            print("Traversing the Queue...")
            while a is not None:
                print("(", a.pri, ",", a.data, ")", end=" ")
                a = a.next
            print()
        else:
            print("Queue is Empty")

    def highest(self):
        if not self.isEmpty():
            return [self.rear.pri,self.rear.data]

    def lowest(self):
        if not self.isEmpty():
            return [self.front.pri,self.front.data]
o = priority_queue()
o.traverse()
o.enqueue(2,"C")
o.enqueue(0,"A")
o.enqueue(1,"B")
o.enqueue(5,"E")
o.traverse()
