# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # 2021.03.21
        # 2nd/4th solution:
        # Find the leaf (a parent node w/o any children) with min depth
        # r.f. no.104 for comparison
        # Note: uncessary to go through the whole BST!
        
        if not root:
            return 0
        min_depth, queue = 0, [(root, 1)]
        while queue:
            p, depth = queue.pop(0)
            min_depth = max(depth, min_depth)
            try:
                assert not p.left is None or not p.right is None
                if p.left:
                    queue.append((p.left, depth + 1))
                if p.right:
                    queue.append((p.right, depth + 1))
            except: # get the leaf nearest to the root
                return min_depth
        
        
        # 3rd solution: recursive
        """
        if not root: return 0
        if not root.left or not root.right:
            return max(self.minDepth(root.left), self.minDepth(root.right)) + 1
        else:
            return min(self.minDepth(root.left), self.minDepth(root.right)) + 1
        """
        
        # 2nd solution: 664 ms (95%) and 92.4 MB (76%)
        # 3rd solution: 844 ms (39%) and 94.7 MB (51%)
        # 4th solution: 668 ms (93%) and 92.4 MB (69%)
        
