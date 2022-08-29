def search(nums, target):
    prev = 0
    step = len(nums) // 4
    prevStep = step
    current = (len(nums) - 1) // 2 
    rotationIdx = ''
    goneOver = False
    while True:
        print(f"Current: {nums[current]}")
        print(f"PrevStep: {prevStep}")
        if current > len(nums) - 1 or len(nums) + current < 0:
            if current > len(nums) - 1 and not goneOver:
                current -= len(nums)
                goneOver = True
            else:
                print("A")
                return -1
        if nums[current] > target and prev < target and max(prevStep, 1) == 1 or nums[current] < target and prev > target and max(prevStep, 1) == 1:
            if rotationIdx == '':
                rotationIdx = current
            elif rotationIdx != current:
                print("B")
                return -1

        if nums[current] > target:
            prev = nums[current]
            current -= max(step, 1)
        elif nums[current] < target:
            prev = nums[current]
            current += max(step, 1)
        else:
            if current >= 0:
                return current
            else:
                return len(nums) + current
        prevStep = step
        step = step // 2


print(search([266,267,268,269,271,278,282,292,293,298,6,9,15,19,21,26,33,35,37,38,39,46,49,54,65,71,74,77,79,82,83,88,92,93,94,97,104,108,114,115,117,122,123,127,128,129,134,137,141,142,144,147,150,154,160,163,166,169,172,173,177,180,183,184,188,198,203,208,210,214,218,220,223,224,233,236,241,243,253,256,257,262,263],208))