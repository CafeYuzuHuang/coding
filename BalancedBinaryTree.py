# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        # a binary tree in which the left and right subtrees of 
        # every node differ in height by no more than 1.
        
        # 2021.03.21
        # 1st solution: DFS, post-order
        # time complexity: O(n), n = # of nodes
        # space complexity: O(hmax), hmax = max depth of BST
        def height(root):
            if not root:
                return 0
            # traversal and propagation of -1
            try:
                lh = height(root.left)
                assert lh != -1
                rh = height(root.right)
                assert rh != -1
            except:
                return -1
            # examine relative height of proximity subtrees
            # max(lh, rh) + 1 is the height from the max depth
            return max(lh, rh)+1 if abs(lh - rh) <= 1 else -1
        return height(root) != -1  
    # 32 ms (97%), 18.8 MB (9%)
    
