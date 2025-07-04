class Solution(object):
    def maxLength(self, arr):
        def is_unique(s):
            return len(set(s)) == len(s)
        def backtrack(i, current):
            if not is_unique(current):
                return 0
            if i == len(arr):
                return len(current)
            include = backtrack(i + 1, current + arr[i])
            skip = backtrack(i + 1, current)
            return max(include, skip)
        return backtrack(0, "")
