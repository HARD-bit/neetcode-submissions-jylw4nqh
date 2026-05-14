class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diff = []
        final_result = []
        for num in nums:
            diff.append(target - num)
        for i, val in enumerate(nums):
            complement = target - val
            if complement in nums:
                j = nums.index(complement)
                if i != j:
                    return sorted([i, j])