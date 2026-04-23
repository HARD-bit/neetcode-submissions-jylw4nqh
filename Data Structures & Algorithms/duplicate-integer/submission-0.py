class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        my_set = set()
        for num in nums:
            my_set.add(num)
        if len(nums) == len(my_set):
            return False
        else: 
            return True
            
        
        

        