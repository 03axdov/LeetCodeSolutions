def intervalIntersection(firstList, secondList):
    idxFirst, idxSecond = 0, 0
    output = []
    if not firstList or not secondList:
        return []
    while True:
        if max(firstList[idxFirst][0], secondList[idxSecond][0]) <= min(firstList[idxFirst][1], secondList[idxSecond][1]):
            output.append([max(firstList[idxFirst][0], secondList[idxSecond][0]), min(firstList[idxFirst][1], secondList[idxSecond][1])])
        if idxFirst < len(firstList) - 1 and idxSecond < len(secondList) - 1:
            if firstList[idxFirst + 1][0] > secondList[idxSecond + 1][0]:
                idxSecond += 1
            else:
                idxFirst += 1
        elif idxFirst == len(firstList) - 1 and idxSecond == len(secondList) - 1:
            break
        elif idxFirst < len(firstList) - 1:
            idxFirst += 1
        elif idxSecond < len(secondList) - 1:
            idxSecond += 1

    return output


print(intervalIntersection([[0,2],[5,10],[13,23],[24,25]], [[1,2]]))