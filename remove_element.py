def removeElement(nums: list, val):
    """
    :type nums: List[int]
    :type val: int
    :rtype: int
    """
    index = 0
    for num in nums:
        if num != val:
            nums[index] = num
            index += 1
    return index

print(removeElement([1,3,2,3,3], 3))