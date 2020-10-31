import random

def seqSearch(ary, data):
    pos = -1

    for i in range(len(ary)):
        if (ary[i] == data):
            pos = i
            break
    
    return pos

def seqSearchMulti(ary, data):
    pAry = []
    for i in range(len(ary)):
        if(ary[i] == data):
            pAry.append(i)
    return pAry


dataAry = [ random.randint(11,99) for _ in range(50) ]
print(dataAry)

position = seqSearch(dataAry, 99)
print(position)

posAry = seqSearchMulti(dataAry, 50)
print(posAry)