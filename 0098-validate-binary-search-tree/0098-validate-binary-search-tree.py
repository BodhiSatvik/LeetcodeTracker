# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
#         def Valid(node, l, r):
#             if not node:
#                 return True
            
#             if not (node.val > l) and (node.val < r):
#                 return False
            
#             return Valid(node.left, l, node.val) and Valid(node.right, node.val, r)
        
#         return Valid(root, float("-inf"), float("inf"))

        def valid(node, left, right):
            if not node:
                return True
            if not (node.val < right and node.val > left):
                return False

            return valid(node.left, left, node.val) and valid(
                node.right, node.val, right
            )

        return valid(root, float("-inf"), float("inf"))