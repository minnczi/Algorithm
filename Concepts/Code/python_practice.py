a = []
def func1(b):
    b += [1]
    print(b)
    return None

func1(a)
print(a)

b = 0
def func2(b):
    b += 1
    return None
func2(b)
print(b)