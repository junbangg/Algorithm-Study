grid = [
    [1, 1, 1, 1, 0, 0],
    [0, 0, 1, 0, 1, 0],
    [0, 0, 1, 0, 1, 0],
    [0, 0, 1, 1, 1, 0],
    [0, 0, 0, 0, 1, 1]
]

def main():
    def getPath(row, col):
        if row < 0 or col < 0 or grid[row][col] != 1:
            return
        isOrigin = row == 0 and col == 0
        if isOrigin or getPath(row-1, col) or getPath(row, col-1):
            path.append((row, col))
            return True
        return False

    if not grid:
        return []
    path = []
    if getPath(len(grid) - 1, len(grid[0]) - 1):
        return path
    return None


print(main())
