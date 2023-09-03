from collections import Counter


class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        rows = map(tuple, grid)
        cols = zip(*grid)
        row_counter = Counter(rows)
        col_counter = Counter(cols)

        answer = 0
        for k, row_v in row_counter.items():
            answer += row_v * col_counter.get(k, 0)

        return answer
