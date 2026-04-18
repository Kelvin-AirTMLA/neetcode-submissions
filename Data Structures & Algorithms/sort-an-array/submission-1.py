class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        n = len(nums)

        if n <= 1:
            return nums

        mid = n // 2

        left_list = self.sortArray(nums[:mid])
        right_list = self.sortArray(nums[mid:])

        return self.merge(left_list, right_list)

    def merge(self, left, right):
        i = 0
        j = 0
        sorted_array = list()
        
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                sorted_array.append(left[i])
                i += 1
            else:
                sorted_array.append(right[j])
                j += 1

        sorted_array.extend(left[i:])
        sorted_array.extend(right[j:])

        return sorted_array
