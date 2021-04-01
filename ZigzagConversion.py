class Solution:
    def convert(self, s: str, numRows: int) -> str:
        # 2021.04.01
        # To complete a zigzag, need 3*numRows-2 for the first one 
        # and 2*(numRows-1) for the following
        
        # 1st solution: naive (sort by raw)
        # https://leetcode.com/problems/zigzag-conversion/solution/
        # time complexity: O(n), space complexity: O(n) (res and listRows)
        """
        if numRows == 1: return s
        if len(s) <= numRows: return s
        
        listRows = ['']*numRows
        curRow = 0
        isGoDown = False
        for c in s: # iterate through the string and sorted by row
            listRows[curRow] += c
            if curRow == 0 or curRow == numRows-1: isGoDown = not isGoDown
            curRow = curRow + 1 if isGoDown else curRow - 1
        
        res = ''
        for ss in listRows:
            res += ss
        return res
        """
        
        # 2nd solution: visit by row
        # https://leetcode.com/problems/zigzag-conversion/solution/
        # time complexity: O(n); space complexity: O(n) (res only)
        
        if numRows == 1: return s
        n = len(s)
        if n <= numRows: return s
        
        res = ''
        nn = 2*(numRows-1) # number of characters to generate a zigzag
        for i in range(numRows): # visit by row
            for j in range(i, n, nn): # go through each zigzag
                res += s[j] # O(1) operation
                k = j+(nn-2*i)
                if i != 0 and i != numRows-1 and k < n:
                    res += s[k]
        return res
        
        # 1st solution: 56 ms (79%), 14.1 MB (97%)
        # 2nd solution: 60 ms (65%), 14.2 MB (88%)
        
