from singlylinkedlist import ListNode


class Linked_List:
    def value_input(self):
        n=int(input("nUMBERS OF Element you want to enter : "))
        self.lst=[]
        for i in range(0,n):
            a=eval(input("Enter input : "))
            self.lst.append(a)
    def buildlist(self,val):
        assert len(val)>0,"no elements"
        a=ListNode(val[0])
        b=a
        for i in range(1,len(val),1):
            b.insert(val[i])
            b=b.next
        return a


    def instail(h, x):
        if h is None:
            return ListNode(x)
        a = h
        while a.next is not None:
            a = a.next
        new = ListNode(x)
        a.next = new
        return h
obj1=ListNode(1)
obj1.insert(2)
obj1.insert(3)
obj1.traverse()
