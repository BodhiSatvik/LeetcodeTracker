class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        if len(s) < 10: return []
        dna = { s[:10]: 1 }
        res = set()
        for i in range(1, len(s)-9):
            seq = s[i:i+10]
            if seq in dna:
                res.add(seq)
            else:
                dna[seq] = 1
        return res
