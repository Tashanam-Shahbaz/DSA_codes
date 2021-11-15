from stackwithlist import mystack
import random


def median_of_three(a, b, c):
    if a <= b and b <= c:
        return b
    if c <= b and b <= a:
        return b
    if a <= c and c <= b:
        return c
    if b <= c and c <= a:
        return c
    return a


def quicksort(list):
    s = mystack()
    n = len(list)
    if n > 1:
        s.push([0, n - 1])

        i = 0
    while not s.isEmpty():
        x = s.pop()
        beg = x[0]
        end = x[1]

        print(list, beg, end)  # uncomment this line to see the step by step working of the algo
        loc = quick(list, beg, end)
        if beg < (loc - 1):
            s.push([beg, loc - 1])
        if (loc + 1) < end:
            s.push([loc + 1, end])


def quick(list, beg, end):
    # x = random.randint(beg, end)
    # y = random.randint(beg, end)
    # z = random.randint(beg, end)
    mid=(beg+end)//2
    loc = median_of_three(beg,mid,end)
    # loc = beg
    left = beg
    right = end
    while True:

        while list[loc] <= list[right] and loc != right:
            right -= 1
        if loc == right:
            return loc
        if list[loc] > list[right]:
            list[loc], list[right] = list[right], list[loc]
            loc = right
        while list[loc] >= list[left] and loc != left:
            left += 1
        if loc == left:
            return loc
        if list[loc] < list[left]:
            list[loc], list[left] = list[left], list[loc]
            loc = left


# mylist = [34, 43, 56, 23, 12, 81, 78, 45, 21, 4, 20, 62]
# mylist=[44,33,11,55,77,90,40,60,99,22,88,66]

mylist = [71, 18, 54, 43, 19, 21]
# mylist=[8,7,6,5,4,3,2,1]
mylist.reverse()
quicksort(mylist)
print(mylist)
