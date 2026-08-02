class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        fmap = {}
        res = [0, 0]
        for i , n in enumerate(nums):
            diff = target - n


            if diff in fmap:
                res = [fmap[diff], i]
                return res

            fmap[n] = i

        return res
