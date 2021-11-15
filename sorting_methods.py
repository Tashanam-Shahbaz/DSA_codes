def selection_sorting(value):
    m = len(value)
    for i in range(m - 1):
        minpos = i
        for j in range(i + 1, m):
            # print(value,minpos,j)
            if value[minpos] > value[j]:
                minpos = j
        if minpos != i:
            value[i], value[minpos] = value[minpos], value[i]
    return value


x = [5, 4, 7, 1, 2]
print(selection_sorting(x))
print()
# x = [7,5,4,2,1]
# print(selection_sorting(x))
# print()
# x = [7,5,4,2,1]
# print(selection_sorting(x))
# print()
# x = [1,2,4,5,7]
# print(selection_sorting(x))

def insertion_sort(values):
    m = len(values)
    for i in range(1, m):
        x = values[i]
        j = i - 1
        print(values, x, i, j)
        while j >= 0 and values[j] > x:
            values[j + 1] = values[j]
            j -= 1
        values[j + 1] = x
    return values


# print(insertion_sort([2, 7, 6, 1, 9, 0]))

def merge(val1, val2):
    n = len(val1)
    m = len(val2)
    print(val1, val2)
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


# my_list = [67, 90, 12, 56, 83, 11, 3, 5, 59, 34, 23]
# my_list=[1,2,3,4,5,6,7,8]
# my_list=[8,7,6,5,4,3,2,1]
# print(merge_sort(my_list))
