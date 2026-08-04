class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned = "".join(filter(str.isalnum, s))
        cleaned = cleaned.lower()

        n = len(cleaned)

        if n <= 1:
            return True

        l = 0
        r = n - 1

        while l < r and cleaned[l] == cleaned[r]:
            l += 1
            r -= 1

            if l >= r:
                return True

        return False
