class Solution:
    def isValid(self, s: str) -> bool:
        


        stack = []

        res = {
            "}": "{",
            ")": "(",
            "]": "[",

        }

        for i, n in enumerate(s):
            if n in res:

                if len(stack) == 0:
                    return False

                if res[n] == stack[-1]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(n)
        
        if len(stack) == 0:
            return True
        return False