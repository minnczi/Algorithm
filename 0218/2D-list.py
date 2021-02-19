lst = [['a', 'b', 'c', 'd', 'e'], [], [], ['f', 'g', 'h', 'i', 'j']]
for i in lst:
    print(*i, end=" ")

# a = map((*i for i in lst), lst)
# print(a)
