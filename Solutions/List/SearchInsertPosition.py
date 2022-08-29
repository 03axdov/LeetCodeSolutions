def searchInsert(nums, target):
    length = len(nums)
    middle = length // 2
    current_index = middle
    current_add = length // 2
    previous = []
    dir = 0

    if current_add == 0:
        current_add = 1

    while True:
        try:
            if current_add > 1:
                current_add = current_add // 2

            print(f"current: {nums[current_index]}")
            print(f"current add: {current_add}")

            if nums[current_index] in previous:
                print(f"Previous: {previous}")
                if dir == 1:
                    return current_index
                else:
                    return current_index + 1
            
            previous.append(nums[current_index])

            if nums[current_index] == target:
                return current_index
            if current_index == 0 and nums[current_index] > target:
                return current_index

            elif nums[current_index] > target:
                current_index -= current_add
                dir = -1
            elif nums[current_index] < target:
                current_index += current_add
                dir = 1
        except IndexError:
            return current_index

print(searchInsert([1], 0))