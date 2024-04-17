class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(s)< len(p):
            return []
        letters = collections.defaultdict(int)
        target = {}
        res = []
        for i in range(len(p)):
            target[p[i]] = 1 + target.get(p[i], 0)
        n = len(p)
        l, r = 0, n-1
        for i in range(n):
            letters[s[i]] = 1 + letters.get(s[i], 0)
        if letters == target:
            res.append(l)
        while r < len(s)-1:
            letters[s[l]] -= 1
            if letters[s[l]] == 0:
                del letters[s[l]]
            l += 1
            r += 1
            if r < len(s):
                letters[s[r]] = 1 + letters.get(s[r], 0)
            if letters == target:
                res.append(l)
        return res

