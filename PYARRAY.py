import ctypes


class Array:
    def __init__(self, n):
        assert n > 0, 'Array size must be > 0'
        self.size = n
        self.elements = (ctypes.py_object * n)()
        self.clear(None)

    def __len__(self):
        return self.size

    def __getitem__(self, index):
        assert 0 <= index < len(self), "Invalid index"
        return self.elements[index]

    def __setitem__(self, index, value):
        assert 0 <= index < len(self), "Invalid index"
        self.elements[index] = value

    def insert(self, index, value):
        for i in range(self.size - 1, index, -1):
            self.elements[i] = self.elements[i - 1]
        self.elements[index] = value

    def delete(self, index):
        for i in range(index, self.size - 1, 1):
            self.elements[i] = self.elements[i + 1]

        self.elements[self.size - 1] = None

    def traverse(self):
        for i in range(len(self)):
            print(self.elements[i], end=" ")
        print()

    def clear(self, value):
        for i in range(len(self)):
            self.elements[i] = value


# myarray = Array(12)
# myarray.traverse()
# stg = "abcdefghijklmnopqrstuvwxyz"
# for i in range(len(myarray)):
#     myarray[i] = stg[i]
# myarray.traverse()
# myarray.delete(7)
# myarray.traverse()
# # myarray.insert(2,"Tashanam")
# # myarray.traverse()
