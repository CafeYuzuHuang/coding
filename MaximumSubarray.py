class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 2021.03.12-13
        # 1st solution: O(N) time complexity (look up on forum ...)
        
        n = len(nums)
        if n == 0:
            return 0
        res = cur = nums[0] # i = 0
        # Since we are only interested in the max sum
        # (not the index range of the subarray)
        # -> if cur < 0, find max value;
        # -> if cur > 0, find max sum ever shown!
        for i in range(1, n):
            if cur > 0:
                cur += nums[i]
            else:
                cur = nums[i]
            if cur > res:
                res = cur
        return res
        
        # 2nd solution: divide-and-conquer algorithm (look up again :( )
        """
        n = len(nums)
        try:
            assert n > 0
        except:
            return 0
        return self.divideAndConquer(nums, 0, n-1)
        """
        # 1st solution runtime 36 ms (100%!!), memory 13.9 MB (95%)
        # 2nd solution runtime 104 ms (5%), memory 14.4 MB (36%)
        # Obviously, any elements in the array are visited more than once during recursion
        # time complexity is O(N^2)
    """
    def divideAndConquer(self, arr, left, right):
        # Used in the 2nd approach
        if left == right:
            return arr[left]
        mid = (left + right) // 2
        left_res = self.divideAndConquer(arr, left, mid)
        right_res = self.divideAndConquer(arr, mid+1, right)
        left_max = arr[mid]
        right_max = arr[mid+1]
        tmp = 0
        for i in range(mid, left-1, -1):
            tmp += arr[i]
            if tmp > left_max:
                left_max = tmp
        tmp = 0
        for j in range(mid+1, right+1, 1):
            tmp += arr[j]
            if tmp > right_max:
                right_max = tmp
        return max(left_res, right_res, left_max+right_max)
    """
