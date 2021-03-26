class Solution:
    def hammingWeight(self, n: int) -> int:
        # 2021.03.26
        # 1st solution: naive, datatype conversion and split by 1
        """
        return len(bin(n)[2:].split('1'))-1
        """
        
        # 2nd solution: bit operation and counting
        count = 0
        for i in range(32):
            if (n & 1): # or define mask = 1, then check if n & mask
                count += 1
            n = n >> 1 # or mask = mask << 1
        return count
        
        
        # 1st solution: runtime 28 ms (90%) and 14.2 MB (42%)
        # 2nd solution: runtime 32 ms (74%) and 14.2 MB (71%)
        
