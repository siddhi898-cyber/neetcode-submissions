class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        char_set = set()      # characters currently inside the window
        left = 0              # left end of window
        max_length = 0        # longest substring found so far

        for right in range(len(s)):          # move right pointer through string
            while s[right] in char_set:      # if current char is already in window
                char_set.remove(s[left])     # remove leftmost character
                left += 1                    # shrink window from left

            char_set.add(s[right])           # add current character to window
            max_length = max(max_length, right - left + 1)  # update answer

        return max_length                    # return longest length
        