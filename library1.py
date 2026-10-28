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
    print("Original Rutherford Occupancy Grid:")
    for row in grid:
        for col in row:
            print(f"{col:>3}", end=" ")
        print()

def main():
    filename = input("Enter occupancy filename: ")
    grid = createGrid(filename)
    displayGrid(grid)

if __name__ == "__main__":
    main()