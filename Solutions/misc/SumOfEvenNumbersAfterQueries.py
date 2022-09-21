def sumEvenAfterQueries(nums, queries):
    even = [num for num in nums if num % 2 == 0]
    sumEven = sum(even)

    output = []

    for query in queries:
        if nums[query[1]] % 2 == 0:
            sumEven -= nums[query[1]]

        nums[query[1]] = nums[query[1]] + query[0]

        if nums[query[1]] % 2 == 0:
            sumEven += nums[query[1]]

        output.append(sumEven)

    return output


print(sumEvenAfterQueries([1,2,3,4], [[1,0],[-3,1],[-4,0],[2,3]]))