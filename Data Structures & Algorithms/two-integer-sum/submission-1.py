class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        exist = {}

        for i in range(len(nums)): # O(n)
            diff = target - nums[i]

            if diff in exist:
                return [exist[diff], i]

            exist[nums[i]] = i