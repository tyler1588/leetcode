class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1

        while True:
            curr = numbers[l] + numbers[r]
            if curr == target:
                break
            if curr > target:
                r -= 1
            if curr < target:
                l += 1
        
        return [l+1, r+1]