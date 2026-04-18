class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = dict()

        for i in range(len(nums)):
            difference = target - nums[i]

            if difference in hash_map:
                return [nums.index(difference), i]

            hash_map[nums[i]] = i
