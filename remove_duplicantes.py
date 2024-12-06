def removeDuplicates(nums: list):
    """
    :type nums: List[int]
    :rtype: int
    """
    nums[:] = sorted(set(nums))
    new_size = len(nums)
    return new_size

print(removeDuplicates([1,1,2]))