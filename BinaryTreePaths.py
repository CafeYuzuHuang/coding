# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        # 2021.03.30
        # 2nd solution: recursive
        """
        if not root.left and not root.right: return [str(root.val)]
        plist = []
        def descPath(root, s):
            if not root: return s
            s_new = s + '->' + str(root.val)
            if not root.left and not root.right: # leaf is reached
                plist.append(s_new)
                return s_new
            return descPath(root.left, s_new), descPath(root.right, s_new)
        descPath(root.left, str(root.val))
        descPath(root.right, str(root.val))
        return plist
        """
        
        # 3rd solution: optimized
        if not root.left and not root.right: return [str(root.val)]
        plist = []
        def descPath(root, s):
            try:
                s_new = s + '->' + str(root.val)
            except: # root is None
                return None
            if not root.left and not root.right: # leaf is reached
                plist.append(s_new)
                return None
            return descPath(root.left, s_new), descPath(root.right, s_new)
        descPath(root.left, str(root.val))
        descPath(root.right, str(root.val))
        return plist
        
        
        # 2nd solution: 36 ms (38%) and 14.2 MB (84%)
        # 3rd solution: 36 ms (38%) and 14.3 MB (31%)
        
