class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        visited = set()
        max_area = 0
        rows, cols = len(grid), len(grid[0])

        def bfs(r, c):
            visited.add((r, c))
            q = collections.deque()
            q.append((r, c))
            area = 1

            while q:
                row, col = q.popleft()
                search = [[1, 0], [-1, 0], [0, 1], [0, -1]]

                for nr, nc in search:
                    r, c = row + nr, col + nc

                    if r in range(rows) and c in range(cols) and (r, c) not in visited and grid[r][c] == 1:
                        area += 1
                        q.append((r,c))
                        visited.add((r, c))
            return area

        for r in range(rows):
            for c in range(cols):
                if (r,c) not in visited and grid[r][c] == 1:
                    max_area = max(max_area, bfs(r, c))
                    
        
        return max_area

# DFS Implementation

# class Solution:
#     def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        



















