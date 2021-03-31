class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # 2021.03.31
        # 1st solution: hash table + slide window
        n = len(s)
        if n <= 1: return n
        rec = {}
        res = 0 # start to last
        tmp = 0 # start index
        for i, c in enumerate(s):
            try:
                tmp = max(tmp, rec[c] + 1)
            except:
                pass
            rec[c] = i # record last index of char c
            res = max(res, i - tmp + 1)
        return res
        
        # 1st solution: 64 ms (65%), 14.3 MB (81%)
        
