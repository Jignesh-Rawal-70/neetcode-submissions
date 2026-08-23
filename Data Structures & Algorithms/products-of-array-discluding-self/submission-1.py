class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left, right = [], [0] * len(nums)
        product = 1
        for num in nums:
            left.append(product)
            product *= num 

        product = 1
        for i in range(len(nums) - 1, -1, -1):
            right[i] = product
            product *= nums[i] 

        for i in range(len(left)):
            left[i] *= right[i]
        return left