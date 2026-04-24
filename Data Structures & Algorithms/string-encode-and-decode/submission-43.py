class Solution:
    def encode(self, strs: List[str]) -> str:
        encoded_arr = []
        for s in strs:
            # 1. Add the length, a '#' delimiter, and the word
            encoded_arr.append(str(len(s)) + "#" + s)
            
        return "".join(encoded_arr)


    def decode(self, s: str) -> List[str]:
        output = []
        i = 0
        
        while i < len(s):
            # 2. Look ahead to find the '#'
            j = i
            while s[j] != "#":
                j += 1
                
            # 3. Everything before the '#' is our length. 
            # This perfectly handles "5", "11", or "150"!
            length = int(s[i:j])
            
            # 4. The word starts exactly one space after the '#'
            word_start = j + 1
            word_end = word_start + length
            
            # 5. Slice out the word and add it to our output
            output.append(s[word_start : word_end])
            
            # 6. Jump our main pointer 'i' forward to the start of the next number
            i = word_end
            
        return output