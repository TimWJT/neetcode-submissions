class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        stack = []
        res = (
            "*",
            "/",
            "+",
            "-"
        )
        for index, t in enumerate(tokens):
            print(t)
            if t in res:
                if len(stack) < 2:
                    return -1

                right = int(stack.pop())
                left = int(stack.pop())
                print(right)
                print(left)

                if t == "*":
                    stack.append(left * right)
         
                elif t == "/":
                    stack.append(left / right)

                elif t == "+":
                    stack.append(left + right)

                elif t == "-":
                    stack.append(left - right)

            else:
                stack.append(t)
            print(stack)
        return int(stack[-1])