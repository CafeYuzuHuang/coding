class Solution:
    def countPrimes(self, n: int) -> int:
        # 2021.03.27 
        # 1st solution: naive, # of prime numbers logn ~ n, where n is int:
        # time complexity O(nlogn)~O(n^2), space O(logn)~O(n)
        """
        if n <= 2: return 0 # 0 and 1 are not prime numbers
        self.primes = [2]
        for i in range(3, n):
            if self.checkPrime(i): self.primes.append(i)
        return len(self.primes)
        
    def checkPrime(self, val):
        j = -1
        i = 2
        lim = val ** 0.5 # upper limit
        while i <= lim and j < len(self.primes):
            try:
                j += 1
                i = self.primes[j]
                assert val % i > 0
            except:
                return False
        return True
        """
        
        # 2nd solution: optimized
        """
        if n <= 2: return 0 # 0 and 1 are not prime numbers
        elif n < 4: return 1 # 2 
        elif n < 6: return 2 # 2, 3 
        elif n < 8: return 3 # 2, 3, 5 
        elif n < 10: return 4 # 2, 3, 5, 7
        self.primes = {2: 2, 3: 3, 5: 5, 7: 7}
        for i in range(9, n, 2): # check odd numbers only
            if self.checkPrime(i): self.primes[i] = i
        return len(self.primes)
        
    def checkPrime(self, val):
        lim = val ** 0.5 # upper limit
        for k, v in self.primes.items():
            try:
                assert val % k > 0
            except:
                return False
            if k > lim: break
        return True
        """
        
        # 3rd solution: see
        # https://leetcode.com/problems/count-primes/discuss/1020029/Python-Solution
        # Assume all numbers are primes, then examine which are not.
        """
        if (n < 3): return 0
        Prime_list = [1] * n
        Prime_list[0] = 0
        Prime_list[1] = 0
        
        for i in range(2,n):
            for j in range (2,n):
                mul = i * j
                if (mul < n):
                    Prime_list[mul] = 0
                else:
                    break
        return (sum(Prime_list))
        """
        
        # 4th solution: optimized
        """
        if (n < 3): return 0
        elif (n < 4): return 1
        elif (n < 6): return 2
        elif (n < 8): return 3
        elif (n < 10): return 4
        Prime_list = [1]*n
        Prime_list[0] = 0
        Prime_list[1] = 0
        
        for i in range(2,n):
            for j in range (i,n):
                mul = i * j
                if (mul < n):
                    Prime_list[mul] = 0
                else:
                    break
        return (sum(Prime_list))
        """
        
        # 5th solution: r.f. https://www.geeksforgeeks.org/sieve-of-eratosthenes/
        # 使用艾氏篩，或稱為質數篩
        return 0 if n < 3 else self.SieveEratosthenes(n-1)
        
    def SieveEratosthenes(self, n):
        prime = [1 for i in range(n+1)]
        prime[0] = False
        prime[1] = False
        p = 2
        while (p*p <= n):
            if (prime[p] == True):
                for i in range(p*p, n+1, p):
                    prime[i] = 0
            p += 1
        return sum(prime)
        
        # 1st solution: time limit exceed
        # 2nd solution: 5268 ms (5%), 27.6 MB (49%)
        # 3rd solution: 4488 ms (7%), 25.5 MB (92%)
        # 4th solution: 2756 ms (12%), 25.5 MB (92%)
        # 5th solution: 472 ms (72%), 34.9 MB (35%)
        
