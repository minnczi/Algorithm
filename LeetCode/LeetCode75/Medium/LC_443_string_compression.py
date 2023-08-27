class Solution:
    # if the letter is not equal to the previous letter,
    # insert the count of prev letter if the count > 0
    def insert_count(self, chars: List[str], i: int, cnt: int) -> List[str]:
        cnt = str(cnt)
        for j in range(len(cnt)):
            chars.insert(i+2+j, cnt[j])
        return chars

    def compress(self, chars: List[str]) -> int:
        prev = ''
        cnt = 1
        # loop the list starting from the end
        # 1) if the letter == previous letter, increase the cnt by 1
        # 2) if not insert the letter count so far (insert_count)
        # 리스트를 거꾸로 순회하면서 중복 글자가 나오는 경우 cnt +1, 아닌경우 현재까지의 글자 카운트 수를 append 한다
        for i in range(len(chars)-1, -1, -1):
            if chars[i] == prev:
                cnt += 1
                chars.pop(i+1)
            else:
                if cnt > 1:
                    self.insert_count(chars, i, cnt)
                prev = chars[i]
                cnt = 1
        if cnt > 1:
            self.insert_count(chars, -1, cnt)
        return len(chars)
