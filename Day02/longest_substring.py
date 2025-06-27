class Solution:
    def lengthOfLongestSubstring(self, s):
        last_seen = [-1] * 128  # ASCII size
        start = 0
        max_len = 0

        for i, char in enumerate(s):
            idx = ord(char)
            if last_seen[idx] >= start:
                start = last_seen[idx] + 1
            last_seen[idx] = i
            max_len = max(max_len, i - start + 1)

        return max_len
