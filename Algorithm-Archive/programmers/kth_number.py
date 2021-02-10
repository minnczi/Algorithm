def solution(array, commands):
    answer = []
    for x in commands:
        arr = array[x[0]-1:x[1]]
        arr.sort()
        arr2 = arr[x[2]-1]
        answer.append(arr2)
    return answer