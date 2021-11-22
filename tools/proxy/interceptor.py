
packet = 0x6a70016a70006d76a6731dc7338dcec69e432b45ceef5d2a00000000


def divide_chunks(l, n):
      
    # looping till length l
    for i in range(0, len(l), n): 
        yield l[i:i + n]

def intercept(data):
    subjectData = list(divide_chunks(data.hex(), 4))
    # print(type(packet   ))

    if subjectData[0] == "6d76":
        # print("before: ", type(subjectData[2]))
        # subjectData[2] = hex(int(subjectData[2], 16)*8)[2:]
        # subjectData[3] = hex(int(subjectData[3], 16)*8)[2:]
        # subjectData[4] = hex(int(subjectData[4], 16)*8)[2:]
        # subjectData[5] = hex(int(subjectData[5], 16)*8)[2:]
        # subjectData[6] = hex(int(subjectData[6], 16)*8)[2:]
        # print("after: ", type(subjectData[2]))
        
        print(" ".join(subjectData))
        interceptedData = bytes("".join(str(subjectData)))
        print(type(interceptedData))
        return interceptedData
    # print(data, "  vs  ", bytes("".join(str(subjectData))))

    return data 
