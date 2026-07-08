class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [0] * n

        prefix = [1] * (n + 1)
        suffix = [1] * (n + 1)
        prefix_sum = 1
        suffix_sum = 1

        for i in range(1, n + 1):
            prefix_sum *= nums[i - 1]
            prefix[i] = prefix_sum

        for i in range(n - 1, -1, -1):
            suffix_sum *= nums[i]
            suffix[i] = suffix_sum

        for i in range(n):
            res[i] = prefix[i] * suffix[i + 1]

        return res
