class Solution:
    def isValid(self, s: str) -> bool:
        
        pairs = {']': '[', '}': '{', ')': '('}
        stack = []
        for c in s:
            if c not in pairs.keys():
                stack.append(c)
            else:
                if len(stack) == 0:
                    return False
                if stack.pop() != pairs[c]:
                    return False
        return len(stack) == 0