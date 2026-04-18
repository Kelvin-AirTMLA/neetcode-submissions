class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        combinations = list()

        combinations.append([]) # for empty array
        def backtrack(combination, index):
            if index >= n: # once index passes the len(nums) we done!
                return
            
            for i in range(index, n):
                number = nums[i]

                combination.append(number) # add number
                combinations.append(combination[:]) # then append immediately to result list
                backtrack(combination, i + 1) # backtrack
                combination.pop() 

        
        backtrack([], 0)
        return combinations
