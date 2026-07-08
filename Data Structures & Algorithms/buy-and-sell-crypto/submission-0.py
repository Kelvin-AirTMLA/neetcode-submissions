class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        best_buying_price = math.inf
        best_selling_price = -math.inf
        best_profit = 0

        for i in range(n):
            best_buying_price = min(best_buying_price, prices[i])
            best_selling_price = max(best_buying_price, prices[i])

            profit = best_selling_price - best_buying_price
            best_profit = max(profit, best_profit)

        return best_profit
