class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # 2021.04.08 revisited
        
        # 1st solution: linear search with time complexity O(n)
        nl = len(needle)
        dif = len(haystack) - nl
        if haystack == "":
            return -1 if needle != "" else 0
        if dif < 0: return -1
        for i in range(dif+1):
            if needle == haystack[i:i+nl]: return i
        return -1
        
        
        # 1st solution: 24 ms (96%) and 14.4 MB (49%)
        
        
