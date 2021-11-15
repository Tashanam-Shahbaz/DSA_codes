class ListNode:
    def __init__(self,data):
        self.data=data
        self.next=None

    def traverse(self):
        a=self
        print("Traversing the list...")
        while a is not None:
            print(a.data,end=" ")
            a=a.next
        print()

    def __len__(self):
        assert self is not None, "Invalid node pointer"
        a = self
        i=0
        while a is not None:
            i+=1
            a = a.next
        return i

    def insert(self, value):
        assert self is not None,"Invalid node pointer"
        n = ListNode(value)
        n.next=self.next
        self.next=n

    def delete(self):
        assert self is not None, "Invalid node pointer"
        x=None
        if self.next is not None:
            tmp=self.next
            x=tmp.data
            self.next=tmp.next
        return x

    def search(self,target):
        assert self is not None,"Invalid node pointer"
        a=self
        if a.data==target:
            return [True, None, a]
        b=a.next
        while b is not None and b.data!=target:
            a=a.next
            b=b.next
        return [b is not None, a, b]

    def circularize(self):
        assert self is not None,"Invalid node pointer"
        a=self
        while a.next is not None:
            a=a.next
        a.next=self

    def traverse_circular(self):
        a = self
        print("Traversing the list...")
        while a.next is not self:
            print(a.data, end=" ")
            a = a.next
        print(a.data, end=" ")
        print()

    def linearize(self):
        assert self is not None, "Invalid node pointer"
        a = self
        while a.next is not self:
            a = a.next
        a.next = None

