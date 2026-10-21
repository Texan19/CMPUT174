def readPackets(filename):
    """
    accepts a filename, reads the content of the packet and excludes blank lines and ERROR's
    :param filename: file
    :return: list
    """
    cleanedPackets = []
    with open(filename, "r") as file:
        for line in file:
            line = line.strip() # strip the \n character
            if line != "ERROR" and line != "":
                cleanedPackets.append(line)

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
        for i in range(numPackets):
            keyStream.append(scrambledPackets.pop(-1))
        return keyStream
    else:
        return None

def packetStrength(packet):
    """
    determine the strength based on the first letter of the packet
    :param packet: str
    :return:
    """
    strength = 0
    if packet[0] == 'X':
        strength = 2
    if packet[0] == 'Z':
        strength = 3
    if packet[0] == 'Q':
        strength = 4
    if packet[0] == 'K':
        strength = 5

    return strength

def keyStreamStrength(keyStream):
    """
    determine the total strength of the keyStream (a list of packets)
    :param keyStream: list
    :return: int
    """
    keyStreamValue = 0
    for packet in keyStream:
        strength = packetStrength(packet)
        keyStreamValue += strength
    return keyStreamValue

def needsBoost(keyStream):
    """
    determine if the key stream needs to be boosted based on its current overall strength rating
    :param keyStream: list
    :return: bool
    """
    keyStreamValue = keyStreamStrength(keyStream)
    if keyStreamValue < 10:
        return True
    else:
        return False

def boostKeyStream(keyStream, scrambledPackets):
    """
    boost the keyStream if the needsBoost is true
    :param keyStream: list
    :param scrambledPackets: list
    :return:
    """
    giveBoost = needsBoost(keyStream)
    if giveBoost and len(scrambledPackets) > 0:
        numPackets = 1
        newPacket = selectPackets(scrambledPackets, numPackets)
        keyStream.extend(newPacket)
    else:
        pass

def compareKeyStreams(chain1, chain2):
    """
    obtains the strength of each chain and compares then against one another
    :param chain1: list
    :param chain2: list
    :return: str
    """
    strength1 = keyStreamStrength(chain1)
    strength2 = keyStreamStrength(chain2)

    if strength1 > 14 and strength2 > 14: # Both > 14
        return "Both are unstable."
    elif strength1 > 14 and strength2 <= 14: #
        return "Chain 2 wins."
    elif strength1 <= 14 and strength2 > 14:
        return "Chain 1 wins."
    elif strength1 <= 14 and strength2 <= 14:
        if strength1 > strength2:
            return "Chain 1 wins."
        elif strength2 > strength1:
            return "Chain 2 wins."
        elif strength1 == strength2:
            return "Tie!"

def main():
    filename = input("Enter the file name: ")
    cleanedPackets = readPackets(filename)
    scrambledPackets = scramble(cleanedPackets)

    while len(scrambledPackets) > 6:
        numPackets = 3
        chain1 = selectPackets(scrambledPackets, numPackets)
        chain2 = selectPackets(scrambledPackets, numPackets)

        print(f"Chain 1 before: {chain1}")
        print(f"Chain 2 before: {chain2}")

        boostKeyStream(chain1, scrambledPackets)
        boostKeyStream(chain2, scrambledPackets)

        print(f"Chain 1 after: {chain1}")
        print(f"Chain 2 after: {chain2}")

        result = compareKeyStreams(chain1, chain2)
        print(result)


if __name__ == "__main__":
    main()
