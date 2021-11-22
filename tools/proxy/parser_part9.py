send = 0
packet = 0x6a70016a70006d76a6731dc7338dcec69e432b45ceef5d2a00000000
server_port=3333
server_host="20.124.113.160"

from termcolor import colored

# before = ['0000', '0000', '0000', '0000', '0000', '0000', '0000', '0000', '0000', '0000', '0000']
def parse(data, port, origin, before):
    # global before
    if port==3333:
        return
    if origin == 'server':
        return
    after = list(divide_chunks(data.hex(), 4))[1:]
    # print(len(after))

    # if len(after) == 10:
    #     deltaVal = delta(before, after)
    #     print(colored("[{}({})]".format(origin, port), 'yellow'), end="\t")
    #     for val in deltaVal:
    #         if val.startswith("+"):
    #             print(colored(val, "blue"), end="\t")
    #         elif val.startswith("-"):
    #             print(colored(val, "red"), end="\t")
    #         else:
    #             print(colored(val, "magenta"), end="\t")
    #     print()


        # print("before: ", before)
        # print("after : ", after)
    return after
    # if send<1:


"""
    





"""

def divide_chunks(l, n):
      
    # looping till length l
    for i in range(0, len(l), n): 
        yield l[i:i + n]

def delta(before: list, after: list) -> list:
    res = []
    for i in range(10):
        temp = int(after[i], 16) - int(before[i], 16)
        if temp > 0:
            res.append("+" + str(temp))
        else:
            res.append(str(temp))

    return res
