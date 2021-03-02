N = 4
def func_B(level):
    if level >= N:
        return
    print(level, end= " ")
    func_B(level+1)
    print(level, end= " ")

func_B(0)