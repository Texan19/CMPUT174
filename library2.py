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
            print(f"{col:>3}", end=" ")
        print()

def findNeighbours(grid, row, col):
    """
    finds neighbours of given cell
    :param grid: 2D list
    :param row: int
    :param col: int
    :return: 1D list
    """
    neighbours = []
    totalRows = len(grid)
    totalCols = len(grid[0])
    for i in range(row-1, row+2): # check the neighboring rows
        for j in range(col-1, col+2): # check the neighboring columns
            if i == row and j == col: # skip the target index
                continue

            if 0 <= i < totalRows and 0 <= j < totalCols: # check boundaries of the grid
                neighbours.append(grid[i][j])

    print(f"Neighbours of zone ({row},{col}) are {neighbours}")

    return neighbours

def fillForWebsite(grid):
    """
    replaces -1 in the gird with the average occupancy of its neighbours
    :param grid: 2D list
    :return: None
    """
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == -1: # find the index where -1 lives
                neighbours = findNeighbours(grid, i, j) # find the neighbors of -1
                averageOccupancy = sum(neighbours)//len(neighbours) # calculate new value for -1 using the average value of its neighbours
                grid[i][j] = averageOccupancy # update -1 with the average value of its neighbours

def main():
    filename = input("Enter occupancy filename: ")
    grid = createGrid(filename)
    print("Original Rutherford Occupancy Grid:")
    displayGrid(grid)

    print()
    fillForWebsite(grid)
    print(f"\nUpdated Rutherford Occupancy Grid:")
    displayGrid(grid)

if __name__ == "__main__":
    main()