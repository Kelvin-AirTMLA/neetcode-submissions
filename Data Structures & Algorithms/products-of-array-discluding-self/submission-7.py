class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)

        prefix = [1] * (n + 1)
        suffix = [1] * (n + 1)
        res = [0] * n

        for i in range(1, n + 1):
            prefix[i] = prefix[i - 1] * nums[i - 1]

        for j in range(n - 1, -1, -1):
            suffix[j] = suffix[j + 1] * nums[j]

        for k in range(n):
            res[k] = prefix[k] * suffix[k+1]

        return res
