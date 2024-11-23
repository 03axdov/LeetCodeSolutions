def merge(nums1, m, nums2, n):
    idx1 = 0    # Keep track of elements waiting to be 'inserted' in resp. list
    idx2 = 0
    current = -1 # Current position in res array
    nums1c = nums1.copy()   # Makes it easier to replace elements in original
    
    while (idx1 < m or idx2 < n):
        current += 1
        
        if idx1 == m:
            nums1[current] = nums2[idx2]
            idx2 += 1
            continue
        if idx2 == n:
            nums1[current] = nums1c[idx1]
            idx1 += 1
            continue
        
        if (nums1c[idx1] < nums2[idx2]):
            nums1[current] = nums1c[idx1]
            idx1 += 1
        else:
            nums1[current] = nums2[idx2]
            idx2 += 1
        
        
    print(nums1)
    
    
merge([1,2,3,0,0,0], 3, [2,5,6], 3)