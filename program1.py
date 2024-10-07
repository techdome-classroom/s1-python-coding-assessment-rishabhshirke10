class Solution:
    def getTotalIsles(self, grid: list[list[str]]) -> int:
        # Dimensions of the grid
        rows, cols = len(grid), len(grid[0])

        # Helper function for DFS traversal
        def dfs(x, y):
            stack = [(x, y)]
            while stack:
                cx, cy = stack.pop()
                grid[cx][cy] = 'W'
                
                for nx, ny in [(cx-1, cy), (cx+1, cy), (cx, cy-1), (cx, cy+1)]:
                    if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] == 'L':
                        stack.append((nx, ny))
        if not grid:
            return 0
        
        island_count = 0
        for i in range(rows):
            for j in range(cols):
                # If we find a land cell ('L'), we have found a new island
                if grid[i][j] == 'L':
                    # Perform DFS to mark the entire island as visited
                    dfs(i, j)
                    # Increment the island count
                    island_count += 1
        
        return island_count
