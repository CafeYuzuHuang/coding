class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        # 2021.03.23
        # Use ASCII code: 65-90
        # chr(65) -> 'A'
        # e.g. XYZ -> 24*26*26 + 25*26 + 26 = 16900
        # -> 16900 = 650*26 = 649*26 + 26 = (24*26 + 25)*26 + 26 -> XYZ
        
        # 1st solution: iterative
        # time and space complexity: O(logN), N = columnNumber
        """
        res = ''
        val = columnNumber
        while True:
            n = val%26
            if n == 0: n = 26
            val -= n
            val //= 26
            res += chr(64 + n)
            if val == 0: return res[::-1]
        """
        
        # 2nd solution: recursive
        def getChr(val):
            n = val%26
            if n == 0: n = 26
            val = (val - n)//26
            return getChr(val) + chr(64 + n) if val > 0 else chr(64 + n)
        return getChr(columnNumber)
        
        # 1st solution: time: 24 ms (95%), memory: 14.3 MB (11%)
        # 2nd solution: time: 28 ms (81%), memory: 14.4 MB (11%)
