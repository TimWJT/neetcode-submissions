class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        

        stack = []
        output = [0] * len(temperatures)


        for i, t in enumerate(temperatures):
            if len(stack) > 0:
                print(stack)
                while len(stack) > 0 and t > temperatures[stack[-1]]:

                    for s in stack:
                        output[s] += 1

                    stack.pop()


            stack.append(i)

        for s in stack:
            output[s] = 0
        return output