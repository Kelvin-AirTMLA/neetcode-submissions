class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        curr = 0
        max_sum = nums[0]

        for i in range(n):
            if curr < 0:
                curr = 0

            curr += nums[i]
            max_sum = max(max_sum, curr)


        return max_sum