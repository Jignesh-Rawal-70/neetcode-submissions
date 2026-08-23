class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        seen = {}
        result = []
        for num in nums:
            seen[num] = seen.get(num, 0) + 1
        
        heap = [(-value, key) for key, value in seen.items()]

        heapq.heapify(heap)
        while k > 0:
            result.append(heapq.heappop(heap)[1])
            k -= 1
        return result