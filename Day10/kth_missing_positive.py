class Solution(object):
    def findKthPositive(self, arr, k):
        missing = 0
        current = 1
        i = 0
        
        while True:
            if i < len(arr) and arr[i] == current:
                i += 1
            else:
                missing += 1
                if missing == k:
                    return current
            current += 1
