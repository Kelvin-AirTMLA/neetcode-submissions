class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashmap = dict()
        count = 1;

        for i in nums:
            hashmap[i] = hashmap.get(i, 0) + 1

            # 1 -> 1
            # 2 -> 1
            # 3 -> 1
            # 3 -> 2
        
        for key in hashmap:
            if hashmap[key] > 1:
                return True

        return False
            