class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        

        res = {} # tuple: longest length, starting index

      
        left = 0

        window_len = 0
        max_freq = 0
        max_length = 0
        

        for right, n in enumerate(s):
            print(n)

            if n not in res:
                res[n] = 0
            res[n] += 1


            max_freq = max(max_freq, res[n])
            window_len = right - left + 1
     
                
            while window_len - max_freq > k:

                res[s[left]] -= 1
                left += 1

                window_len = right - left + 1
            
        max_length = max(max_length, window_len)

        print(left)
        print(s[left + 1])
        return max_length
            
# a b a b b b a     k = 2
#   ^         ^

# a
# a b
# a b a
# a b a b
# b a b b
# b a b b a



            

