import array as arr

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        chars = set()
        official_letter_count_map = dict()
        
        
        for letter in s:
            chars.add(letter)
            official_letter_count_map[letter] = official_letter_count_map.get(letter, 0) + 1

        for letter in t:
            if letter not in chars or t.count(letter) < official_letter_count_map[letter] or t.count(letter) > official_letter_count_map[letter]:
                return False

        return True