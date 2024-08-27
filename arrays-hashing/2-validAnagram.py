class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dict = {}
        for c in s:
            dict[c] = 1 + dict.get(c, 0)
        for c in t:
            dict[c] = dict.get(c, 0) - 1
        for key in dict.keys():
            if dict[key] != 0:
                return False
        return True