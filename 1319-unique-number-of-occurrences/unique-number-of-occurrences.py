class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        a = collections.Counter(arr)
        ase = set()
        for v in a.values():
            print(v)
            if v in ase:
                return False
            ase.add(v)
        return True
        