class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        multiplier = ""
        for letter in s:
            if letter == "]":
                # "["가 나올때까지 글자를 합친후 앞의 숫자만큼 곱한다
                # 최종 결과물을 다시 stack 안에 넣는다
                repeated_str = ""
                while True:
                    top = stack.pop()
                    if isinstance(top, int):
                        stack.append(repeated_str * top)
                        break
                    else:
                        repeated_str = top + repeated_str
            elif letter.isnumeric():
                multiplier += letter
            elif letter == "[":
                stack.append(int(multiplier))
                multiplier = ""
            else:
                stack.append(letter)
        return "".join(stack)
