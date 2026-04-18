

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        n = len(strs)
        
        prefix = strs[0]

        for i in range(n):
            while not strs[i].startswith(prefix):
                prefix = prefix[:-1]

        return prefix
