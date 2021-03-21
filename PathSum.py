# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def hasPathSum(self, root, targetSum):
        """
        :type root: TreeNode
        :type targetSum: int
        :rtype: bool
        """
        # 2021.03.21
        # 4th solution:
        # Edge cases
        if not root:
            return False
        que = list([(root, root.val), ])
        while que:
            p, pv = que.pop(0)
            # check targetsum only if one leaf node is reached
            if pv == targetSum and not p.left and not p.right:
                return True
            if p.left:
                que.append((p.left, pv + p.left.val))
            if p.right:
                que.append((p.right, pv + p.right.val))
        return False
    
    # 4th solution: 32 ms (76%) and 17.2 MB (19%)
    
