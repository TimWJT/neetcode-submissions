class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        char_count = {}
        max_freq = 0
        left = 0
        max_length = 0
        
        for right in range(len(s)):
            # Add right character
            if s[right] not in char_count:
                char_count[s[right]] = 0
            char_count[s[right]] += 1
            
            # Track max frequency in current window
            max_freq = max(max_freq, char_count[s[right]])
            
            # Current window length
            window_len = right - left + 1
            
            # Shrink window if changes needed > k
            while window_len - max_freq > k:
                char_count[s[left]] -= 1
                left += 1
                window_len = right - left + 1
            
            # Update result
            max_length = max(max_length, window_len)
        
        return max_length

# Example: s = "ababba", k = 2
# Expected: 5 (change to "aaaa" or "bbbbb" with 2 changes)