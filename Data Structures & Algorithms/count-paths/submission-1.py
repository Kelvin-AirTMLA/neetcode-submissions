class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        memo = dict()

        def dfs(i: int, j: int) -> int:
            if i <= 0:
                return 0

            if j <= 0:
                return 0

            if i == 1:
                return 1
            
            if j == 1: return 1

            if (i, j) in memo:
                return memo[(i, j)]

            left = dfs(i, j - 1)
            right = dfs(i - 1, j)

            res = left + right

            memo[(i, j)] = res
            return res

        return dfs(m, n)
