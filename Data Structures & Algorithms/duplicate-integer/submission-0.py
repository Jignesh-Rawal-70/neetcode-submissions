class Solution:
    def hasDuplicate(self, nums) -> bool:
        seen: set[int] = set()
        for i in nums:
            if i in seen:
                return True
            else:
                seen.add(i)
        return False