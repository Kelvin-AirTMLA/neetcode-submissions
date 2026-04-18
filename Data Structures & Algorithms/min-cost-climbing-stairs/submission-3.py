class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        dp = [0] * n

        dp[0] = cost[0]
        dp[1] = cost[1]

        minimum_cost = 1e9

        for i in range(2, n):
            dp[i] = cost[i] + min(dp[i - 1], dp[i - 2])
            print(dp[i])

        minimum_cost = min(dp[n - 1], dp[n - 2])
        return minimum_cost
