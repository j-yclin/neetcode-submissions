from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        counter_map = Counter(s)
        for c in t:
            counter_map[c] -= 1
        for i in counter_map.values():
            if i != 0:
                return False
        return True
