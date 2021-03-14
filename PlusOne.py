class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        # 2021.03.14
        # 2nd solution: naive dtype conversion, O(N) complexity
        # the target is to find 9, and notice the size change
        # e.g.1: [9, 9, 9, 9] -> [1, 0, 0, 0, 0]
        # e.g.2: [8, 7, 9] -> [8, 8, 0]
        # e.g.3: [1, 0, 0, 0] -> [1, 0, 0, 1]
        """
        p_one = [] # output array
        n = len(digits)
        num = 0
        for i in range(n):
            num += digits[i] * 10**(n - i - 1)
        return [int(i) for i in str(num+1)]
        """
        # 3rd solution: simulate the "ADD" algorithm
        # If digits is allowed to be modified, use this
        
        n = len(digits)
        c = 1 # the added value
        for i in range(n-1, -1, -1):
            if digits[i] + c >= 10:
                c = 1
                digits[i] = 0
            else:
                digits[i] += c
                c = 0
        if c == 1:
            digits = [c] + digits
        return digits
        
        # 2nd solution: 16 ms (92%) and 13.3 MB (73%)
        # 3rd solution: 20 ms (71%) and 13.2 MB (99%)
