class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        seen_characters = set()
        longest_substring_found = 0
        left = 0
        
        for right in range(len(s)):

            while s[right] in seen_characters:

                seen_characters.remove(s[left])
                left +=1
            
            seen_characters.add(s[right])
            longest_substring_found = max(longest_substring_found, len(seen_characters))

        return longest_substring_found
            
            