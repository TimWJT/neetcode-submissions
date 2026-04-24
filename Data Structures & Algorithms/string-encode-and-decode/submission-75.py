class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_arr = []
        for s in strs:
            length = str(len(s))
            encoded_arr.append(length)
            encoded_arr.append("#")
            encoded_arr.append(s)
            
        return "".join(encoded_arr)

    def decode(self, s: str) -> List[str]:

        if not s:  
            return []
            
        output = []
        next_word_length_index = 0 
        next_word_length_arr = []
        char_array = []
        i = 0
        hashtag_flag = False
        
        while i < len(s):

            if hashtag_flag == False and s[i] == "#":
                
                # THE FIX: Calculate the exact index of the NEXT number
                # Current position (i) + length of the word + 1
                word_length = int("".join(next_word_length_arr))
                next_word_length_index = i + word_length + 1

                hashtag_flag = True
        
            elif hashtag_flag == False:
                next_word_length_arr.append(s[i])
                
            elif hashtag_flag == True and i == next_word_length_index:
                if i != 0:
                    output.append("".join(char_array))
                    char_array = []  
                
                    hashtag_flag = False
                    next_word_length_arr = []
                    next_word_length_arr.append(s[i])

            else:
                char_array.append(s[i])

            i += 1
            
        if s:
            output.append("".join(char_array))
        
        return output