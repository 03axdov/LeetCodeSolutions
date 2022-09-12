import math
from collections import deque
def adolescentArchitecture(n, blocks):

    def getBaseSides(block):
        if block[0] == 'cube':
            return block[1]
        else:
            return block[1] * 2**0.5

    cubeBases = deque(sorted([getBaseSides(block) for block in blocks if block[0] == 'cube'], reverse=True))
    cylinderBases = deque(sorted([getBaseSides(block) for block in blocks if block[0] == 'cylinder'], reverse=True))

    output = []
    while cubeBases or cylinderBases:
        if len(output):
            print(f"output: {output}")
            if len(cubeBases) == 0:
                base = cylinderBases.popleft()
                if output[-1][1] < base: return 'impossible'
                output.append(['cylinder', base])
            elif len(cylinderBases) == 0:
                base = cubeBases.popleft()
                print(base)
                if output[-1][1] < base: return 'impossible'
                output.append(['cube', base])
            else:
                if min(cubeBases[0], cylinderBases[0]) > output[-1][1]: return 'impossible'
                if cubeBases[0] > cylinderBases[0]:
                    base = cubeBases.popleft()
                    output.append(['cube', base])
                else:
                    base = cylinderBases.popleft()
                    output.append(['cylinder', base])

        else:
            if len(cubeBases) == 0:
                base = cylinderBases.popleft()
                output.append(['cylinder', base])
            elif len(cylinderBases) == 0:
                base = cubeBases.popleft()
                output.append(['cube', base])
            else:
                if cubeBases[0] > cylinderBases[0]:
                    base = cubeBases.popleft()
                    output.append(['cube', base])
                else:
                    base = cylinderBases.popleft()
                    output.append(['cylinder', base])

    for i in output:
        if i[0] == 'cylinder':
            i[1] /= 2**0.5
            i[1] = int(i[1])
    return output

print(adolescentArchitecture(3, [
    ('cube', 5),
    ('cylinder', 3),
]))