class Solution:
    # def hasDuplicate(self, nums: List[int]) -> bool:
    #     unique = set()
    #     for num in nums:
    #         if num in unique:
    #             return True
    #         else:
    #             unique.add(num)
    #     return False
    
    def hasDuplicate(self, nums):
        nums.sort()
        for i in range(len(nums) - 1):
            if nums[i] == nums[i+1]:
                return True
        return False
