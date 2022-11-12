# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        arr = []
        
        def sol(node, arr):
            # while len(arr) < k:
            if node:
                sol(node.left, arr)
                arr.append(node.val)
                sol(node.right, arr)
            return arr
         
        return sol(root, arr)[k-1]