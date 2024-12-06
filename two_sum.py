class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i == j:
                    continue
                if nums[i] + nums[j] == target:
                    return [i, j]

    def twoSumOptimized(self, nums, target):
        nums_vistos = {}
        for i, valor in enumerate(nums):
            diferenca = target - valor

            if diferenca in nums_vistos:
                print(nums_vistos)
                return [i, nums_vistos[diferenca]]
            else:
                nums_vistos[valor] = i
