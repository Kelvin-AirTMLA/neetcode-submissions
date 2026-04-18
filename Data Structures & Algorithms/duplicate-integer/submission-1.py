class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        freq_count = dict()

        for i in range(len(nums)):

            if nums[i] in freq_count:
                return True

            freq_count[nums[i]] = i

        return False
