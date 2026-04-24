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

        res = []

        i = 0

        while i < len(s):
            
            j = i

            while s[j] != "#":
                j += 1
            
            string_length = int(s[i:j])



            res.append(s[j + 1: j + 1 + string_length])
            i = j + 1 + string_length

        return res


#     def decode(self, s: str) -> List[str]:


#         if not s:  
#             return []
            
#         output = []
#         next_word_length_index = 0 
#         next_word_length = 0
#         next_word_length_arr = []
#         char_array = []
#         i = 0
#         hashtag_flag = False
        
#         while i < len(s):


#             if hashtag_flag == False and s[i] == "#":
#                 print(next_word_length_arr)
#                 # next_word_length_index = int("".join(next_word_length_arr))
#                 # next_word_length_index = next_word_length_index + len(next_word_length_arr) + 1

#                 word_length = int("".join(next_word_length_arr))
#                 next_word_length_index = i + word_length + 1
#                 hashtag_flag = True
        
                
# ###   5#hello5#world
#             elif hashtag_flag == False:
#                 next_word_length_arr.append(s[i])
                
            
#             elif hashtag_flag == True and i == next_word_length_index:
#                 if i != 0:
#                     output.append("".join(char_array))
#                     char_array = []  
                
                
#                     hashtag_flag = False
#                     next_word_length_arr = []
#                     next_word_length_arr.append(s[i])


                
#             else:
#                 char_array.append(s[i])
            

#             i += 1
            
#         if s:
#             output.append("".join(char_array))
        
#         if output == ["","",""]:
#             print(s)
#         return output