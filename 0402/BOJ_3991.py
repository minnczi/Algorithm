import sys
sys.stdin = open('3991_input.txt', 'r')

h, w, c = map(int, input().split())
colors = list(map(int, input().split()))

board = [[0] * w for _ in range(h)]

row = col = 0
dc = 1
for i in range(len(colors)):
    color_num = i+1
    for _ in range(colors[i]):
        board[row][col] = color_num
        col += dc
        
        if col >= w:
            row += 1
            col -= 1
            dc = -1
        
        elif col < 0:
            row += 1
            col += 1
            dc = 1

print(board)
