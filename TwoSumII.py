def twoSum(numbers: [int], target: int) -> [int]:
    right = len(numbers) - 1
    left = 0
    output = []
    while left < right:
        if numbers[left] + numbers[right] == target:
            return [left + 1, right + 1]
        elif numbers[left] + numbers[right] < target:
            left += 1
        else:
            right -= 1

print(twoSum([0,0,3,4],0))