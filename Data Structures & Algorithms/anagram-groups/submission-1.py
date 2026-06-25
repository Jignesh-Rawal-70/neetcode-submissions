class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen = defaultdict(list)

        for s in strs:
            c = [0] * 26
            for ch in s:
                index = ord(ch) - ord('a')
                c[index] += 1
            seen[tuple(c)].append(s)
        return list(seen.values())