class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        # 2021.03.16:
        # Note: the returned dtype is int, input is non-negative int
        
        # 3rd solution: brute force
        # Since x^0.5 < x/2 and x > 1, try 1 <= x <= x/2
        """
        if x <= 1:
            return x
        # for i in range(1, x//2+1): -> cause memory error
        i = 0
        k = x//2
        while i < k:
            i += 1
            n = (i+1) ** 2 - x
            if n == 0:
                return i+1
            m = i ** 2 - x
            if m * n < 0:
                return i
        return 1
        """
        # 4th solution: short cut
        """
        return int(x ** 0.5)
        """
        
        # 9th solution: Newton-Raphson method
        # f(a) = a^2 - x, f'(a) = 2a
        # -> 0 - f(a0) = f'(a0) * (a1 - a0) -> a1 = -f(a0)/f'(a0) + a0
        # For sqrt: a1 = -(a0^2 - x)/(2*a0) + a0
        """
        if x <= 1:
            return x
        n_digits = len(str(x))
        a0 = 10 ** (n_digits // 2) # initial guess
        tol_err = 1e-6
        err = 1.0
        i = 0
        imax = 1000
        while err > tol_err:
            i += 1
            f = float(a0) ** 2 - float(x)
            fb = (float(a0)*(1.0 - tol_err)) ** 2 - float(x) # backward
            ff = (float(a0)*(1.0 + tol_err)) ** 2 - float(x) # forward
            fp = (ff - fb)/(2 * float(a0) * tol_err) # slope
            a1 = float(a0) - f/fp
            err = abs(a1/a0 - 1.0)
            a0 = a1
            if i > imax:
                return -999 # deverged
        return int(a0) # converged
        """
        
        # 10th solution: Newton-Raphson method
        # f(a) = a^2 - x, f'(a) = 2a
        # -> 0 - f(a0) = f'(a0) * (a1 - a0) -> a1 = -f(a0)/f'(a0) + a0
        # For sqrt: a1 = -(a0^2 - x)/(2*a0) + a0 = a0/2 + x/(2a0)
        """
        if x <= 1:
            return x
        n_digits = len(str(x))
        a0 = 10 ** (n_digits // 2) # initial guess
        tol_err = 1e-6
        err = 1.0
        i = 0
        imax = 1000
        while err > tol_err:
            i += 1
            a1 = float(a0)/2.0 + float(x)/(2.0*float(a0))
            err = abs(a1/a0 - 1.0)
            a0 = a1
            if i > imax:
                return -999 # deverged
        return int(a0) # converged
        """
        
        # 11th solution: binary search
        # time complexity: O(logN)
        
        if x <= 1:
            return x
        n_a = len(str(x))//2
        a_low = 0
        a_up = 10 ** (n_a + 1) # to reduce the search range
        while a_low <= a_up:
            a_mid = (a_low + a_up) // 2
            f = a_mid ** 2
            if f == x:
                return a_mid
            if f > x:
                a_up = a_mid - 1
            else:
                a_low = a_mid + 1
        return a_up # crossed, return lower value
        
        
        # 3rd solution: 5600 ms (5%), 13.5 MB (37%)
        # 4th solution: 12 ms (98%), 13.4 MB (66%)
        # 9th solution: 20 ms (79%), 13.3 MB (66%)
        # 10th solution: 28 ms (40%), 13.5 MB (13%)
        # 11th solution: 12 ms (98%), 13.3 MB (90%) **
        
