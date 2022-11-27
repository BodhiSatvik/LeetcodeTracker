# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        
        def sumCal(node, maxPath):
            if not node:
                return [0, maxPath]
            
            l, m1 = sumCal(node.left, maxPath)
            r, m2 = sumCal(node.right, maxPath)
            maxPath = max(m1, m2)

            maxPath = max(maxPath, node.val + l + r)
            bestPath = max(node.val + l, node.val + r, 0)


            return [bestPath, maxPath]
        
        return sumCal(root, root.val)[1]