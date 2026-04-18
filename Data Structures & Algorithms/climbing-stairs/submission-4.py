class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        
        memo = {1:1, 2:2}

        def climb(n):
            if n in memo:
                return memo[n]
            else:
                memo[n] = climb(n - 2) + climb(n - 1)
                return memo[n]

        return climb(n)
