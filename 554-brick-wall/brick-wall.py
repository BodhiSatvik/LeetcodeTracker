class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        gaps = { 0: 0 }
        for row in wall:
            total = 0
            for b in row[:-1]:
                total += b
                if total in gaps:
                    gaps[total] += 1
                else:
                    gaps[total] = 1

        return len(wall) - max(gaps.values())
                