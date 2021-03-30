# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # 2021.03.30
        # at least 2 nodes exist in the BST
        # p and q are UNEQUAL, and all nodes are UNIQUE!
        # BST can be in-order traversed.
        
        # 2nd solution: recursion / r.f. solution
        # NOTE: p or q can be far deeper than LCA
        """
        r_val, p_val, q_val = root.val, p.val, q.val
        if p_val > r_val and q_val > r_val: # right subtree
            return self.lowestCommonAncestor(root.right, p, q)
        elif p_val < r_val and q_val < r_val: # left subtree
            return self.lowestCommonAncestor(root.left, p, q)
        else: # root is LCA, including root as decestor
            return root
        """
        
        # 3rd solution: iterative
        node, p_val, q_val = root, p.val, q.val
        while node:
            n_val = node.val
            if min(p_val, q_val) > n_val: # right subtree
                node = node.right
            elif max(p_val, q_val) < n_val: # left subtree
                node = node.left
            else: # node is LCA, including node as decestor
                return node
        # 2nd solution: 76 ms (73%), 18.3 MB (30%)
        # 3rd solution: 76 ms (73%), 18.4 MB (30%)
        
        # Time complexity: O(N)
        # Space complexity: recursive O(N) for skewed BST, iterative O(1)
        
