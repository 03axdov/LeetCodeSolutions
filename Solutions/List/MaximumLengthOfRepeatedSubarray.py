def findLength(nums1, nums2) -> int:
    string2 = ''.join([chr(num) for num in nums2])
    string1 = ''
    output = 0

    for num in nums1:
        string1 += chr(num)

        if string1 in string2:
            output = max(output, len(string1))
        else:
            string1 = string1[1:]

    return output

print(findLength([0,0,0,0,1], [1,0,0,0,0]))