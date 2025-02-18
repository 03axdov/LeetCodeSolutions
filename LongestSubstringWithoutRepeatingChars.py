class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()
        left = 0  # Left pointer for the sliding window
        maxLength = 0  # Store the maximum length

        for right in range(len(s)):
            while s[right] in charSet:
                charSet.remove(s[left])  # Remove leftmost character to maintain uniqueness
                left += 1  # Move left pointer forward

            charSet.add(s[right])  # Add new character to the set
            maxLength = max(maxLength, right - left + 1)  # Update the maximum length
        
        return maxLength
