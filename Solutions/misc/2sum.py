def twosum(li, target):
    dic = {}
    for t, i in enumerate(li):
        if i in dic.keys():
            return (dic[i], t)
        else:
            dic[target - i] = t
    return None


print(twosum([1,2,3,4,5], 1))