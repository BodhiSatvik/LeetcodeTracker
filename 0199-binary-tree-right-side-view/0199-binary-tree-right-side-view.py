# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# class Solution:
#     def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
#         res = []
#         q = collections.deque()
#         low = 0
        
#         if root:
#             q.append([root,1])
            
#         while q:
#             for i in range(len(q)):
#                 node, level = q.pop()
                
#                 if level > low:
#                     res.append(node.val)
#                     low = level

#                 if node.left:
#                     q.append([node.left, level+1])
                
#                 if node.right:
#                     q.append([node.right, level+1])
        
#         return res
class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        res = []
        q = collections.deque([root])

        while q:
            rightSide = None
            qLen = len(q)

            for i in range(qLen):
                node = q.popleft()
                if node:
                    rightSide = node
                    q.append(node.left)
                    q.append(node.right)
            if rightSide:
                res.append(rightSide.val)
        return res
                    
                
            