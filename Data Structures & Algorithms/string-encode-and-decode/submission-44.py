class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_arr = []
        for s in strs:
            # FIX 1: We MUST add a '#' here so your decoder knows where numbers end.
            length = str(len(s))
            encoded_arr.append(length + "#") 
            encoded_arr.append(s)
            
        return "".join(encoded_arr)


    def decode(self, s: str) -> List[str]:
        if not s:  # Handle empty string to avoid LeetCode type errors
            return []
            
        output = []
        char_array = []
        
        # This tracks the exact index where we expect to find the NEXT number.
        next_word_length_index = 0
        
        i = 0
        while i < len(s):
            
            # If our current index matches the index where a number should be:
            if i == next_word_length_index:
                
                # FIX 2: Check 'i != 0' instead of 'if char_array:'. 
                # This allows your code to successfully save empty strings!
                if i != 0:
                    output.append("".join(char_array))
                    char_array = []  # Clear the array for the next word
                    
                # FIX 3: Read forward until we hit the '#'. 
                # This handles lengths of 1, 10, or 100 perfectly without crashing!
                j = i
                while s[j] != '#':
                    j += 1
                length_of_word = int(s[i:j])
                
                # Calculate exactly where the NEXT number will be.
                # 'j' is the index of the '#'. The word starts exactly at j + 1.
                next_word_length_index = (j + 1) + length_of_word
                
                # Fast-forward our main pointer 'i' to the '#' symbol. 
                # When the loop finishes, 'i += 1' will land it perfectly on the first letter!
                i = j
                
            # Otherwise, we are looking at a letter. Add it to the array.
            else:
                char_array.append(s[i])
                
            i += 1
            
        # Once the loop finishes, append the very last word we built
        if s:
            output.append("".join(char_array))
            
        return output