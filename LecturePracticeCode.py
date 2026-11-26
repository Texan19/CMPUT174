
grid = [
    ['#', '.', '.', '#'],
    ['.', 'X', '.', '.'],
    ['#', '.', 'X', '.'],
    ['.', '.', '.', '#']
]

def count_in_row(grid):
    totalCount = 0
    for i in range(len(grid)):
        rowCount = 0
        for j in range(len(grid[0])):
            if grid[i][j] == 'X':
                rowCount += 1
                totalCount += 1
        print(f"Row{i}: {rowCount}")
    print(f"TotalCount: {totalCount}")


count_in_row(grid)
