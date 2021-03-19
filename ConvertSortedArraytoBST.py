# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        # 2021.03.19
        # 1st solution: recursive, divide-and-conquer
        # Build a binary tree from sorted array with two
        # subtrees that |max_depth_1 - max_depth_2| <= 1
        # Ascending sorted array -> inorder-traversed binary tree
        def grow(l, r):
            if l > r:
                return None
            m = l + (r - l) // 2
            tree = TreeNode(nums[m])
            tree.left = grow(l, m-1)
            tree.right = grow(m+1, r)
            return tree
        return grow(0, len(nums)-1) 
    
    # 1st solution: 56 ms (100%) and 15.6 MB (100%) !!!!!
    # Key points:
    # (1) combined with binary search
    # (2) use function wrapper
    # (3) time complexity: O(n), space complexity: O(logn)
    # where n = lengths of sorted array
    
