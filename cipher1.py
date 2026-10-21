def readPackets(filename):
    """
    accepts a filename, reads the content of the packet and excludes blank lines and ERROR's
    :param filename: file
    :return: list
    """
    file = open(filename, 'r')
    content = file.readlines()
    file.close()
    cleanedPackets= []

    for lines in content:
        lines = lines.strip() # strip the \n character

        if lines != "ERROR" and lines != "":
            cleanedPackets.append(lines)

    return cleanedPackets

def scramble(cleanedPackets):
    """
    splits the packets into a left and right section and creates a new list that scrambles the left and right sections
    :param cleanedPackets: list
    :return: list
    """
    scrambledPackets = []
    splitIndex = len(cleanedPackets) // 2 # find the middle index of the list

    leftSide = cleanedPackets[:splitIndex] # split the list from 0 to the middle index
    rightSide = cleanedPackets[splitIndex:] # split the list from 0 to the last index

    while len(leftSide) != 0 and len(rightSide) != 0:
        scrambledPackets.append(leftSide.pop(-1)) # the last index of the left becomes an index of scrambled packets
        scrambledPackets.append(rightSide.pop(-1)) # the last index of the right becomes an index of scrambled packets

    return scrambledPackets

def selectPackets(scrambledPackets, numPackets):
    """
    goes through the scrambled list and returns a certain amount of items
    :param scrambledPackets: list
    :param numPackets: int
    :return: list or str or None
    """
    keyStream = []

    if len(scrambledPackets) >= numPackets: # if our list is bigger than the number of packets to be dealt with
        if numPackets == 1:
            packetString = scrambledPackets.pop(-1)
            return packetString
        elif numPackets > 1:
            for i in range(numPackets):
                keyStream.append(scrambledPackets.pop(-1))
            return keyStream
    else:
        return None

def main():
    filename = input("Enter the file name: ")
    cleanedPackets = readPackets(filename)
    scrambledPackets = scramble(cleanedPackets)
    numPackets = 6
    keyStream = selectPackets(scrambledPackets, numPackets)
    print(keyStream)

if __name__ == "__main__":
    main()
