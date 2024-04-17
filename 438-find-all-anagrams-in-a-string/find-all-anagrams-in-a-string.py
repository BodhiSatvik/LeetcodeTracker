class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        ns, np = len(s), len(p)
        if ns < np:
            return []

        countS, countP = collections.Counter(), collections.Counter(p)
        res = []

        for i in range(ns):
            countS[s[i]] += 1

            if i >= np:
                if countS[s[i-np]] == 1:
                    del countS[s[i-np]]
                else:
                    countS[s[i-np]] -= 1
            if countP == countS:
                res.append(i-np+1)
        return res
