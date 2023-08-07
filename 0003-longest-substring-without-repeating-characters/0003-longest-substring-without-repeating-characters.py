class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s == "": return 0
        if len(s) == 1: return 1
        res = 1
        l = 0
        while l < len(s):
            sub = set(s[l])
            r = l+1
            while (r < len(s)) and (s[r] not in sub):
                sub.add(s[r])
                r += 1
            res = max(res, len(sub))
            l += 1
        return res
