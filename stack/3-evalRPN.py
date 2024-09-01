class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        keys = {"+", "-", '/', '*'}

        for token in tokens:
            if token not in keys:
                stack.append(token)
            else:
                b = stack.pop()
                a = stack.pop()
                c = int(eval(f"{a} {token} {b}"))
                stack.append(c)
        return int(stack[0])