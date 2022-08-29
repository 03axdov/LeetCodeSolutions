def combinationSum4(nums, target):
    sub_targets = [[] for i in range(target)]
    result = 0
    nums = sorted(nums)

    for num in nums:
        if num < target:
            sub_targets[num].append(num)
            for li in sub_targets:
                for i in li:
                    if num + i < target:
                        print(f"1 num: {num}")
                        print(f"1 i: {i}")
                        sub_targets[num+i].append(num+i)
                    if num + i == target:
                        print(f"2 num: {num}")
                        print(f"2 i: {i}")
                        result += 1
        if num == target:
            
            result += 1
    print(f"sub_targets: {sub_targets}")
    return result


print(combinationSum4([3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25], 10))

    