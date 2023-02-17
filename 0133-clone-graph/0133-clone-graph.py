"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        dupe = {}

        def dfs(node):
            # Base case
            if node in dupe:        # Check if that node has already been added to our duplicate tracker
                return dupe[node]   # Return the copy we made of that node
            
            # Recursive case
            copy = Node(node.val)   # Create deep copy of node with just its value
            dupe[node] = copy       # Assign copy as value to the old node key in tracker

            for neighbor in node.neighbors:
                copy.neighbors.append(dfs(neighbor))
            
            return copy
        
        return dfs(node) if node else None



            