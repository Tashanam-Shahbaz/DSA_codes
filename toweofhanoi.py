def toh(num,first,middle,last):
    if num==1:
        print("Move disk from",first,"to",last)
        return
    toh(num-1, first, last,middle)
    toh(1, first, middle, last)
    toh(num-1,middle,first, last)
toh(4,"A","B","C")