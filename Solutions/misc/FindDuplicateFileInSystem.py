from collections import defaultdict
def findDuplicate(paths):
    files = defaultdict(list) # value: [path(s)]
    output = []

    for path in paths:
        pathList = path.split(" ")
        for p in pathList[1:]:
            p = p.replace(")", "")
            p = p.split("(")
            files[p[-1]].append(pathList[0] + "/" + p[0])

    for value, paths in files.items():
        if len(paths) > 1:
            output.append(paths)

    return output


print(findDuplicate(["root/a 1.txt(abcd) 2.txt(efgh)","root/c 3.txt(abcd)","root/c/d 4.txt(efgh)","root 4.txt(efgh)"]))
