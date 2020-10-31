import random

def binSearch(ary, data):
    pos = -1
    start = 0
    end = len(ary) - 1
    count = 0

    while start <= end:
        count += 1
        mid = (start+end) // 2
        if ary[mid] == data:
            return mid
        elif ary[mid] < data:
            start = mid + 1
        else:
            end = mid - 1
    print(count)
    return pos


dataAry = [ random.randint(10000, 99999) for _ in range(1000000) ]
dataAry.sort()

print(binSearch(dataAry, 11111))