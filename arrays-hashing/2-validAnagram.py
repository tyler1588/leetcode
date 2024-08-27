class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sd, st = {}, {}

        if len(s) != len(t):
            return False

        for i in range(len(s)):
            sd[s[i]] = sd.get(s[i], 0) + 1
            st[t[i]] = st.get(t[i], 0) + 1

        for element in sd:
            if sd.get(element) != st.get(element):
                return False

        return True