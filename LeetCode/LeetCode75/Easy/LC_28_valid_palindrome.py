class Solution:
    def isPalindrome(self, s: str) -> bool:
        word = ""
        for i in s:
            if i.isalpha():
                word += i.lower()
            elif i.isnumeric():
                word += i
        return word == word[len(word)-1::-1]