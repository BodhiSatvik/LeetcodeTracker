# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        def rser(node, string):
            if node is None:
                string += 'N,'
            else:  
                string += str(node.val) + ','
                string = rser(node.left, string)
                string = rser(node.right, string)
            return string
        
        return rser(root, '')

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        def rdeser(l):
            if l[0] == 'N':
                l.pop(0)
                return None
            root = TreeNode(l[0])
            l.pop(0)
            root.left = rdeser(l)
            root.right = rdeser(l)
            return root
            
            
        l = data.split(",")
        return rdeser(l)
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))