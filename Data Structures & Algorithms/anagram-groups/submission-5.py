from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = list()
        mp = dict()

        for i in range(len(strs)):
            s = strs[i] # get each word
            s = "".join(sorted(s))

            if s not in mp:
                mp[s] = len(res)
                res.append(list())
        
            res[mp[s]].append(strs[i])
    
        return res