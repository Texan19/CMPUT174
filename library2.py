def createGrid(filename):
    """
    creates a 2D list of occupancy grid
    :param filename: file
    :return: 2D list
    """
    with open(filename, "r") as file:
        content = file.readlines()

    rows = int(content[0])
    cols = int(content[1])
    lines = []

    for line in content:
        lines.append(line.split())

    lines.pop(0)
    lines.pop(0)

    grid = []

    for i in range(rows):
        rowList = []
        for j in range(cols):
            rowList.append(int(lines[i][j]))
        grid.append(rowList)

    return grid

def displayGrid(grid):
    """
    displays a grid of occupancy grid
    :param grid: 2d list
    :return: None
    """
    for row in grid:
        for col in row:
            print(col, end=" ")
        print()

def findNeighbors(grid, row, col):
    """
    finds neighbors of given cell
    :param grid: 2D list
    :param row: int
    :param col: int
    :return: 1D list
    """
    neighbors = []
    totalRows = len(grid)
    totalCols = len(grid[0])
    for i in range(row-1, row+2): # check the neighboring rows
        for j in range(col-1, col+2): # check the neighboring columns
            if i == row and j == col: # skip the target index
                continue

            if 0 <= i < totalRows and 0 <= j < totalCols: # check boundaries of the grid
                neighbors.append(grid[i][j])

    print(f"Neighbors of ({row}, {col}) are {neighbors}")

    return neighbors

def fillForWebsite(grid):
    """
    replaces -1 in the gird with the average occupancy of its neighbors
    :param grid: 2D list
    :return: None
    """
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == -1:
                neighbors = findNeighbors(grid, i, j)
                averageOccupancy = sum(neighbors)//len(neighbors)
                grid[i][j] = averageOccupancy

def main():
    filename = input("Enter occupancy file name: ")
    grid = createGrid(filename)
    displayGrid(grid)
    fillForWebsite(grid)
    displayGrid(grid)

if __name__ == "__main__":
    main()