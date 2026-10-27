def partition_packets(packet_list):
    listQ = []
    listNoQ = []

    for packet in packet_list:
        if packet[0] == "Q":
            listQ.append(packet)
        else:
            listNoQ.append(packet)

    print(listQ)
    print(listNoQ)


packet_list = [
    "XQQ",
    "QZK",
    "QXK",
    "KKQ",
    "KZX",
    "QXZ",
    "XKQ"
]

partition_packets(packet_list)