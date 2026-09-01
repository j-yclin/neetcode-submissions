from collections import Counter, defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)
        for s in strs:
            c = Counter(s)
            key = tuple(sorted(c.items()))
            groups[key].append(s)
        return list(groups.values())