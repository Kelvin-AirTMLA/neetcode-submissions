class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hash_map = dict()
        res = list()
        max_record = 0
        record = list()

        for i in range(len(nums)):

            number = nums[i]

            if number not in hash_map:
                hash_map[number] = len(res)
                res.append(list())

            res[hash_map[number]].append(number)

        print(res)
        top_k = [res[0] for res in sorted(res, key=len, reverse=True)[:k]]

            
        return top_k