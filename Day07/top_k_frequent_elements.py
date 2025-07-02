import heapq
from collections import Counter

class Solution:
    def topKFrequent(self, nums, k):
        freq = Counter(nums)
        return [item for item, _ in heapq.nlargest(k, freq.items(), key=lambda x: x[1])]
