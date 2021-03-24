class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        # 2021.03.24
        # Use ord() function to get ascii code from a character
        
        # 1st solution:
        val = 0
        for i, c in enumerate(columnTitle):
            val *= 26
            val += ord(c) - 64
        return val
        
        # time: 32 ms (75%), memory: 14.4 MB (13%)
        
        
        
