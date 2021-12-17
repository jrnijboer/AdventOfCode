from math import prod
line = open("../input/day16.input", encoding="utf-8").read().strip()
hex = int(line, 16)
inputBits = bin(hex)[2:]

if line[0] == "0":
    if line[1] in "123":
        inputBits = "00" + inputBits
    elif line[1] in "4567":
        inputBits = "0" + inputBits
    inputBits = "0000" + inputBits
if line[0] in "123":
    inputBits = "00" + inputBits
if line[0] in "4567":
    inputBits = "0" + inputBits

V, Subs, Literals = {}, {}, {}
def readPacket(pos: int, data: str, packetCount: int):
    count = 0
    while count < packetCount:
        count += 1
        version = int(data[pos:pos + 3], 2)
        V[pos] = version
        type = int(data[pos + 3: pos + 6], 2)
        if type == 4:  # literal
            posLiteral = pos
            pos += 6
            keepReading = True
            value = ""
            while keepReading:
                value += data[pos + 1:pos + 5]
                pos += 5
                if data[pos - 5] == "0":
                    keepReading = False
            Literals[posLiteral] = int(value, 2)

        else:  # operator
            operatorPosition = pos
            id = data[pos + 6]
            subpackets = []
            if id == "0":  # bitlength for packets in the next 15 bits
                length = int(data[pos + 7:pos + 22], 2)
                pos += 22
                pos, res = readPacketBits(pos, data, pos + length)
                subpackets = res
            else:  # number of packets in the next 11 bits
                subpackets = []
                nr = int(data[pos + 7:pos + 18], 2)
                pos += 18
                while nr > 0:
                    subpackets.append(pos)
                    pos = readPacket(pos, data, 1)
                    nr -= 1
            Subs[operatorPosition] = (type, subpackets)
    return pos

def readPacketBits(pos: int, data: str, bits: int):
    subs = []
    while pos < bits:
        subs.append(pos)
        pos = readPacket(pos, data, 1)
    return pos, subs

Ops = {
    0: lambda subs: sum(getPacketValue(v) for v in subs),
    1: lambda subs: prod(getPacketValue(v) for v in subs),
    2: lambda subs: min(getPacketValue(v) for v in subs),
    3: lambda subs: max(getPacketValue(v) for v in subs),
    5: lambda subs: 1 if getPacketValue(subs[0]) > getPacketValue(subs[1]) else 0,
    6: lambda subs: 1 if getPacketValue(subs[0]) < getPacketValue(subs[1]) else 0,
    7: lambda subs: 1 if getPacketValue(subs[0]) == getPacketValue(subs[1]) else 0}

def getPacketValue(key):
    if key not in Subs:
        return Literals[key]
    operator, subs = Subs[key]
    return Ops[operator](subs)

readPacket(0, inputBits, 1)
print("Answer A:", sum(V.values()))
print("Answer B:", getPacketValue(0))
