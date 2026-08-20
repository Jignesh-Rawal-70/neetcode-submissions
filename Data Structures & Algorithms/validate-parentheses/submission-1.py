class Solution:
    def isValid(self, s: str) -> bool:
        match = {')':'(', '}':'{', ']':'['}
        stack = []
        for ch in s:
            if len(stack) == 0 and ch not in match:
                stack.append(ch)
            else:
                #if open brace then push to stack
                if ch not in match:
                    stack.append(ch)
                #if closed brace, then pop and compare
                elif not stack or stack.pop() != match[ch]:
                    return False

        return len(stack) == 0