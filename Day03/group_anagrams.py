from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs):
        anagrams = defaultdict(list)

        for word in strs:
            key = tuple(sorted(word))  # Sorting makes all anagrams have the same key
            anagrams[key].append(word)

        return list(anagrams.values())
