def createGrid(filename):
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

    print(grid)

def main():
    createGrid("occupancy1.txt")

if __name__ == "__main__":
    main()