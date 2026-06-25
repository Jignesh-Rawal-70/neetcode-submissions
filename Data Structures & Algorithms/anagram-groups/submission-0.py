class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen = {}
        result = []
        for token in strs:
            sorted_token = sorted(token)
            sorted_token_str = ''.join(sorted_token)
            current_list = seen.get(sorted_token_str, [])
            current_list.append(token)
            seen[sorted_token_str] = current_list
        
        for value in seen.values():
            result.append(value)
        return result