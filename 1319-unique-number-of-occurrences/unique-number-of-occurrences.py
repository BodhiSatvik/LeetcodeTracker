class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        # a = collections.Counter(arr)
        # ase = set()
        # for v in a.values():
        #     if v in ase:
        #         return False
        #     ase.add(v)
        # return True
        # freq = {}
        # for x in arr:
        #     freq[x] = freq.get(x, 0) + 1
        cnt = Counter(arr)     
        x = cnt.values()
        y = set(x)
        return len(x) == len(y)

        return len(freq) == len(set(freq.values()))
        