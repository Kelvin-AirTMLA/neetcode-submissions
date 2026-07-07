class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        exists_by_index = {}
        res = [0,0]

        for i, n in enumerate(nums):
            diff = target - n

            if diff in exists_by_index:
                res = [exists_by_index[diff], i]
                return res

            exists_by_index[n] = i
