class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l < r:
            mid = (l + r) // 2
            if nums[mid] > nums[r]:
                l = mid + 1
            else:
                r = mid
        pivot = r

        #search left subarray
        result_left = self.binary_search(nums[0:pivot], target)
        result_right = self.binary_search(nums[pivot:], target)

        if result_left != -1:
            return result_left
        if result_right != -1:
            return pivot + result_right
        return -1


    def binary_search(self, nums, target):
        l, r = 0, len(nums) - 1

        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                r = mid - 1
            else:
                l = mid + 1
        return -1