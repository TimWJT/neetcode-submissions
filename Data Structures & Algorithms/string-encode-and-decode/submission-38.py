class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_arr = []
        for s in strs:
            
            length = str(len(s))

            encoded_arr.append(length)
            encoded_arr.append("#")

            encoded_arr.append(s)
            
            
            # my current string
        return "".join(encoded_arr)



    def decode(self, s: str) -> List[str]:
            output = []
            i = 0
            
            while i < len(s):
                # 1. Find where the '#' is
                j = i
                while s[j] != "#":
                    j += 1
                    
                # 2. The number before the '#' is our length
                length = int(s[i:j])
                
                # 3. The word starts right after the '#'
                word_start = j + 1
                word_end = word_start + length
                
                # 4. Slice the word out and add it to our output
                output.append(s[word_start : word_end])
                
                # 5. Jump 'i' forward to the start of the next number
                i = word_end
                
            return output