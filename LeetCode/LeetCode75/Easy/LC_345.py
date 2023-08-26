class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]

        vowel_list = []
        vowel_pos = []
        all_letter_list = []
        for i in range(len(s)):
            if s[i] in vowels:
                vowel_list.append(s[i])
                vowel_pos.append(i)
            all_letter_list.append(s[i])

        vowel_list.reverse()

        for i in range(len(vowel_list)):
            all_letter_list[vowel_pos[i]] = vowel_list[i]

        return "".join(all_letter_list)
