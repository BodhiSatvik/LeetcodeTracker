class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if collections.Counter(s) != collections.Counter(t):
            return False
        return True