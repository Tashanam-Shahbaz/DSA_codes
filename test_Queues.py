# from priorityqueuewithlinkedlist import *
# x = [[2, 3], [1, 7], [5, 4], [5, 8],
# [1, 4], [3, 1]]
# my_pq = priority_queue()
# for i in range(len(x)):
#     my_pq.enqueue(x[i][0], x[i][1])
# my_pq.traverse()
# print("removing", my_pq.dequeue())
# my_pq.traverse()
# print("removing", my_pq.dequeue())
# my_pq.traverse()
# my_pq.enqueue(2, 7)
# my_pq.enqueue(6, 8)
# my_pq.enqueue(4, 9)
# my_pq.enqueue(4, 8)
# my_pq.enqueue(1, 5)
# my_pq.traverse()
# print("removing", my_pq.dequeue())
# my_pq.traverse()
# print("highest", my_pq.highest())
# print("lowest", my_pq.lowest())
# pq2 = priority_queue()
# pq2.enqueue(2, 3)
# pq2.enqueue(1, 6)
# pq2.enqueue(3, 5)
# pq2.traverse()
# pq2.enqueue(2, 7)
# pq2.traverse()

def merge(val1, val2):
    n = len(val1)
    m = len(val2)
    if n == 0:
        return val2
    if m == 0:
        return val1
    val = []
    i = 0
    j = 0
    while i < n or j < m:
        if i == n:
            val.extend(val2[j:])
        return val
    if j == m:
        val.extend(val1[i:])
        return val
    if val1[i] <= val2[j]:
        val.append(val1[i])
        i += 1
    else:
        val.append(val2[j])
        j += 1
def merge_sort(values):
    m = len(values)
    if m <= 1:
        return values
    n = m // 2
    val1 = merge_sort(values[0:n])
    val2 = merge_sort(values[n:])
    val = merge(val1, val2)
    return val
my_list = [67, 34, 90, 12, 56, 83, 11, 3, 5,
59, 34, 23]
print(merge_sort(my_list))