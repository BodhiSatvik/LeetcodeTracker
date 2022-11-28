# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        maxPath = root.val
        
        def sumCal(node):
            nonlocal maxPath
            
            if not node:
                return 0
            
            l = max(sumCal(node.left), 0)
            r = max(sumCal(node.right), 0)

            maxPath = max(maxPath, node.val + l + r) 
            return node.val + max(l, r)
        
        sumCal(root)
        return maxPath