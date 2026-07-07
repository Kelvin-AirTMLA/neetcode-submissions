class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        n = len(s)
        m = len(t)
        hm_s = {}
        hm_t = {}

        if n != m:
            return False

        for char in s:
            hm_s[char] = hm_s.get(char, 0) + 1

        for char in t:
            hm_t[char] = hm_t.get(char, 0) + 1

        return hm_t == hm_s
