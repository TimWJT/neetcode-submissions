class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        if len(s2) < len(s1):
            return False

        res_set = set()

        res = {}

        for n in s1:
            
            if n not in res:
                res[n] = 0
                res_set.add(n)
            res[n] += 1


        left = 0
        right = len(s1) - 1

        while right < len(s2):
            # print("window: " + str(s2[left:right+1]))

            i = left
            while i <= right:
                

                # print("current letter: " + str(s2[i]))
                # print("current set: " + str(res_set))
                # print("current res: " + str(res))
                if s2[i] not in res:
                    break
                

                res[s2[i]] -= 1

                if res[s2[i]] == 0:
                    # print("removed: " + str(s2[i]))
                    res_set.remove(s2[i])
                i += 1


            if len(res_set) == 0:
                return True

            else:
                # print("resettinggggggg")
                print(str(res_set))
                res = {}
                for n in s1:
                    
                    if n not in res:
                        res[n] = 0
                        res_set.add(n)
                    res[n] += 1
                print(str(res))

            
            left += 1
            right += 1

        return False