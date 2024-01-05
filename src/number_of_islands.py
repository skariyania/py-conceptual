def number_of_island(grid):
    if not grid:
        return 0

    def dfs(i, j):
        if i < 0 or i >= m or j < 0 or j >= n or grid[i][j] == '0':
            return
        grid[i][j] = '0'  # Mark the current cell as visited
        # Explore neighbors in all four directions
        dfs(i + 1, j)
        dfs(i - 1, j)
        dfs(i, j + 1)
        dfs(i, j - 1)

    m, n = len(grid), len(grid[0])
    island_count = 0

    for i in range(m):
        for j in range(n):
            if grid[i][j] == '1':
                island_count += 1
                dfs(i, j)

    return island_count

# Example 1
grid1 = [
    ["1", "1", "1", "1", "0"],
    ["1", "1", "0", "1", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "0", "0", "0"]
]
print(number_of_island(grid1))  # Output: 1

# Example 2
grid2 = [
    ["1", "1", "0", "0", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "1", "0", "0"],
    ["0", "0", "0", "1", "1"]
]
print(number_of_island(grid2))  # Output: 3
