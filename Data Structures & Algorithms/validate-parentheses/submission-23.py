class Solution:
    def isValid(self, s: str) -> bool:
        

        res = {"}":"{", 
            ")":"(", 
            "]":"["
            }   

        stack = []

        
        for i, n in enumerate(s):
            print(stack)
            print(n)

            if len(stack) == 0:
                stack.append(n)
                continue

            if n in res:
                if stack[-1] == res[n]:
                    # print(stack)
                    stack.pop()
                else:
                    return False
            else:
                print("appending" + n)
                stack.append(n)

        print(len(stack))
        if len(stack) == 0:
            return True
        return False
        

