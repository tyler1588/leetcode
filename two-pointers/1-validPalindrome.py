class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1
        while l < r:
            while not self.alphaNum(s[l]) and l < r:
                l += 1
            while not self.alphaNum(s[r]) and r > l:
                r -= 1
            if s[l].lower() != s[r].lower():
                return False
            l, r = l + 1, r - 1
        return True

    def alphaNum(self, s):
        return s.isalpha() or s.isdigit()
        