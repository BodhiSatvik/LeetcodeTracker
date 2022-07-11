class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(set(s)) == len(set(t)) == len(set(zip(s, t))):
            return True
        else:
            return False