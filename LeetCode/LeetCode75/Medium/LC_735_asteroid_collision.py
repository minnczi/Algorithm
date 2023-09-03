class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for num in asteroids:
            stack.append(num)

            while len(stack) >= 2:
                left_num, right_num = stack[-2], stack[-1]
                left_sign = 1 if left_num > 0 else -1
                right_sign = 1 if right_num > 0 else -1
                if left_sign == 1 and right_sign == -1:
                    print(left_num, right_num, left_sign, right_sign)
                    if abs(left_num) == abs(right_num):
                        stack.pop()
                        stack.pop()
                    elif abs(left_num) > abs(right_num):
                        stack.pop(-1)
                    elif abs(left_num) < abs(right_num):
                        stack.pop(-2)
                        continue
                break
        return stack
