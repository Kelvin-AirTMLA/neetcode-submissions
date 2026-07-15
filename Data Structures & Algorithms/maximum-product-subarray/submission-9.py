class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # take [-4, 5, -3] && [2, 4, -3, 5]
        
        res = nums[0]
        curMin, curMax = 1, 1

        for n in nums:
            tmp = curMax * n
            curMax = max(n * curMax, n * curMin, n)
            curMin = min(tmp, n * curMin, n)
            res = max(res, curMax)

        return res
 