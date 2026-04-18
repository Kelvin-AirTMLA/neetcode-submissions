class Solution:
    def scoreOfString(self, s: str) -> int:
        score = 0
        difference = 0
        n = len(s)
        

        for left in range(n - 1):
            right = left + 1
            difference = ord(s[right]) - ord(s[left])
            score += abs(difference)

        return score
