class Solution:
    def isValid(self, s: str) -> bool:
        close = {
           ")": "(",
           "}": "{",
           "]": "[" 
        }
            
        stack = []
        
        for c in s:
            if c in close:
                if stack and stack[-1] == close[c]:
                    stack.pop(-1)
                else:
                    return False
            else:
                stack.append(c)
        return True if not stack else False