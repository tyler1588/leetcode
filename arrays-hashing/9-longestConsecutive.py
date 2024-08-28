class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        
        res = 0
        for n in s:
            if n - 1 not in s:
                tmp = 1
                while n + tmp in s:
                    tmp += 1
                res = max(res, tmp)
        return res