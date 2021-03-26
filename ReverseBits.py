class Solution:
    def reverseBits(self, n: int) -> int:
        # 2021.03.26
        # 1st solution: naive
        """
        i = 0
        sr = ''
        val = n
        while i < 32:
            sr += str(val % 2)
            val -= int(sr[-1])
            val //= 2
            i += 1
        i = 0
        val = 0
        while i < 32:
            val *= 2
            val += int(sr[i])
            i += 1
        return val
        """
        
        # 2nd solution: optimized
        # time complexity O(1), space complexity O(1) 
        # (since length of bits is fixed)
        """
        val = 0
        for i in range(32):
            val *= 2
            try:
                assert n % 2 == 0
            except:
                val += 1
                n -= 1
            n //= 2
        return val
        """
        
        # 3rd solution (r.f. leetcode solution)
        # Mask-and-shift solution, no loop necessary!
        # Both time and space complexity are still O(1)
        
        # Use bitwise shift operators << and >>, and bit logical operators & and |:
        # divide 32-bit n into two parts, then switch then, and update record in n:
        n = (n >> 16) | (n << 16)
        # 0x -> hexadecimal; 
        # 0xff = 255 (11111111), 0xff00 = 65280 (1111111100000000)
        # divide into 4 8-bit parts, masked by 0xff00ff00 or 0x00ff00ff, 
        # then switch the position and record into n.
        n = ((n & 0xff00ff00) >> 8) | ((n & 0x00ff00ff) << 8)
        # repeat ...
        # 0xcc = 0b11001100, 0xaa = 0b10101010
        n = ((n & 0xf0f0f0f0) >> 4) | ((n & 0x0f0f0f0f) << 4)
        n = ((n & 0xcccccccc) >> 2) | ((n & 0x33333333) << 2)
        n = ((n & 0xaaaaaaaa) >> 1) | ((n & 0x55555555) << 1)
        return n
        
        # 1st solution: runtime 48 ms (8%), memory 14.1 MB (71%)
        # 2nd solution: runtime 36 ms (37%), memory 14 MB (91%)
        # 3rd solution: runtime 28 ms (89%), memory 14.1 MB (91%)
        
