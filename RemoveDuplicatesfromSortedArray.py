def Duplicates(nums:[int]):
    nums.sort()
    print(nums)

    i = 1
    j = len(nums)
    while i < j:
        if nums[i] == nums[i - 1]:
            nums.pop(i - 1)
            j = j - 1
            continue
        i = i + 1

    return len(nums)


print(Duplicates([1,1,2,5,8,6,8,9,2,5]))