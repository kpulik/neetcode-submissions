class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if i == j:
                    pass
                elif nums[i] + nums[j] == target:
                    sol = [i,j]
                    return sol
        