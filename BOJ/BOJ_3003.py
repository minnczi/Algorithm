correct_chess_set = [1, 1, 2, 2, 2, 8]
given_chess_set = list(map(int, input().split()))

print(" ".join([str(correct_chess_set[i] - given_chess_set[i]) for i in range(6)]))