from collections import Counter


class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        cnt1, cnt2 = Counter(word1), Counter(word2)

        # 조건1: 글자끼리 자리를 바꿔서 같은 단어를 만들수 있으려면, 가지고 있는 전체 글자의 set이 같아야함
        if set(cnt1.keys()) == set(cnt2.keys()):
            # 조건2: 한 글자를 모두 다른 글자로 바꿔야하기 때문에, 두 단어간의 글자들의 등장 횟수가 같아야함
            if sorted(cnt1.values()) == sorted(cnt2.values()):
                return True

        return False
