class Solution:
    def isUgly(self, n: int) -> bool:
        # 2021.03.30
        # 1st solution:
        # Ugly number not great than 2x3x5 = 30:
        # (1), 2, 3, 4, 5, 6, 8, 9, 10, 12, 15, 16, 18, 20, 24, 25, 27, 30
        # only 7, 11, 13, 14, 17, 19, 21, 22, 23, 26, 28, 29 is not
        # time complexity: O(logn*k*logn), space complexity: O(k)
        # where k is # of ugly numbers within 30
        # k*logn in time complexity comes from the mod operation in the for loop
        """
        if n <= 0: return False
        un = [30,27,25,24,20,18,16,15,12,10,9,8,6,5,4,3,2,1]
        
        def checkUN(n):
            if n > 30:
                for i in un[:-1]:
                    if n%i == 0: return checkUN(n//i)
            else:
                return True if n in un else False
        return checkUN(n)
        """
        
        # 2nd solution: optimized?
        """
        if n <= 0: return False
        un = [30,27,25,24,20,18,16,15,12,10,9,8,6,5,4,3,2,1]
        un2 = [30, 15, 6, 5, 3, 2]
        
        def checkUN(n):
            if n > 30:
                for i in un2:
                    if n%i == 0: return checkUN(n//i)
            else:
                return True if n in un else False
        return checkUN(n)
        """
        
        # 4th solution:
        if n <= 0: return False
        while n > 1:
            if n%2 == 0: n = n//2
            elif n%3 == 0: n = n//3
            elif n%5 == 0: n = n//5
            else: return False
        return True
        
        # 1st solution: 32 ms (33%) and 14.5 MB (12%)
        # 2nd solution: 36 ms (33%) and 14.4 MB (12%)
        # 4th solution: 32 ms (64%) and 14.3 MB (12%)
        
