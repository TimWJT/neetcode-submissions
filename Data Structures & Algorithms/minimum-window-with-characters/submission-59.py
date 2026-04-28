class Solution:
    def minWindow(self, s: str, t: str) -> str:
        

        res = {}

        unseen_letters = set()

        for n in t:
            unseen_letters.add(n)
            if n not in res:
                res[n] = 0
            res[n] += 1
        

        min_str = ""
        min_str_length = float('inf')

        left = 0
        for right, n in enumerate(s):
            print(n)
            if n in res:
                res[n] -= 1
                print("current res: " + str(res))
                if res[n] <= 0 and n in unseen_letters:
                    unseen_letters.remove(n)
                    print("unseen: " + str(unseen_letters) + " referring to this letter: " + n)
         
            while len(unseen_letters) == 0:
                # We have a valid window, try to shrink it
                # Save the current window before shrinking
                if right - left + 1 < min_str_length:
                    min_str = s[left:right+1]
                    min_str_length = len(min_str)
                
                # Check if removing left character breaks the window
                if s[left] in res:
                    res[s[left]] += 1
                    if res[s[left]] > 0:  # We now need more of this char
                        unseen_letters.add(s[left])
                        res[s[left]] -= 1  # Put it back
                        break
                    else:  # We still have enough (count <= 0)
                        left += 1
                else:
                    left += 1
            # print("printing res: " + str(res))
            # print("current string: " + str(s[left:right+1]))
                    
            
                    
        return min_str

    #     xymxxyz

    # xyz