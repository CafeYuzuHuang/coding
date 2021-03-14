class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        # 2021.03.14
        # 3rd solution: simulate BINARY ADD algorithm
        """
        m = len(a)
        n = len(b)
        add0s = ''
        for i in range(abs(m-n)):
            add0s += '0'
        if m > n:
            b = add0s + b
        else:
            a = add0s + a
        c = ''
        x = '0'
        # Eight possible conditions:
        # a[i] b[i]   x   -> c[i]  x
        #  '0'  '0'  '0'     '0'  '0'
        #  '0'  '0'  '1'     '1'  '0'
        #  '1'  '0'  '0'     '1'  '0'
        #  '1'  '0'  '1'     '0'  '1' *
        #  '0'  '1'  '0'     '1'  '0'
        #  '0'  '1'  '1'     '0'  '1' *
        #  '1'  '1'  '0'     '0'  '1' *
        #  '1'  '1'  '1'     '1'  '1' **
        for i in range(max(m, n)-1, -1, -1):
            if a[i] == b[i]:
                c += x
                x = '0' if a[i] == '0' else '1'
            else:
                c = c + '1' if x == '0' else c + '0'
        if x == '1':
            return '1' + c[::-1]
        else:
            return c[::-1]
        """
        
        # 4th solution: to optimize 3rd
        """
        m = len(a)
        n = len(b)
        add0s = ''
        for i in range(abs(m-n)):
            add0s += '0'
        if m > n:
            b = add0s + b
        else:
            a = add0s + a
        c = ''
        x = '0'
        # Eight possible conditions:
        # a[i] b[i]   x   -> c[i]  x
        #  '0'  '0'  '0'     '0'  '0'
        #  '1'  '0'  '0'     '1'  '0'
        #  '0'  '1'  '0'     '1'  '0'
        #  '0'  '0'  '1'     '1'  '0'
        #  '1'  '1'  '0'     '0'  '1' *
        #  '1'  '0'  '1'     '0'  '1' *
        #  '0'  '1'  '1'     '0'  '1' *
        #  '1'  '1'  '1'     '1'  '1' **
        for i in range(max(m, n)-1, -1, -1):
            gg = len( [i for i in [a[i], b[i], x] if i == '0'] )
            c = c + '0' if gg%2 == 1 else c + '1'
            x = '0' if gg > 1 else '1'
            
        if x == '1':
            return '1' + c[::-1]
        else:
            return c[::-1]
        """
        
        # 5th solution: use int (if overflow issue does not matter)
        # Binary-integer conversion:
        # int = sum( bin[i] * 2^i ), i from 0 to n-1
        # e.g. '1011' = 1 x 2^0 + 1 x 2^1 + 0 x 2^2 + 1 x 2^3 = 1 + 2 + 0 + 8 = 11
        """
        int_a = 0
        int_b = 0
        m = len(a)
        n = len(b)
        o = max(m, n)
        add0s = ''
        for i in range(abs(m-n)):
            add0s += '0'
        if m > n:
            b = add0s + b
        else:
            a = add0s + a
        for i in range(o):
            int_a += int(a[i]) * 2 ** (o - i - 1)
            int_b += int(b[i]) * 2 ** (o - i - 1)
        int_c = int_a + int_b
        c = ''
        for i in range(o+1):
            q = int_c // 2
            r = int_c % 2
            c += str(r)
            int_c = q
        if c[-1] == '0':
            return c[-2::-1]
        else:
            return c[::-1]
        """
        
        # 6th solution: short-cut for python!
        return bin(int(a, 2) + int(b, 2))[2:] # drop-off the beginning "0b"
        
        # 3rd solution: 24 ms (62%) and 13.5 MB (55%)
        # 4th solution: 28 ms (39%) and 13.6 MB (55%)
        # 5th solution: 32 ms (21%) and 13.6 MB (23%)
        # 6th solution: 16 ms (94%) and 13.5 MB (55%)
