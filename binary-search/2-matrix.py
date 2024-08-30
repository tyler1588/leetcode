class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for row in matrix: 
            l, r = 0, len(row)-1
            if target >= row[l] and target <= row[r]:
                return self.binarySearch(row, l, r, target)
        return False
        
    def binarySearch(self, row, l, r, target):
        while l <= r:
            mid = (l + r) // 2
            if row[mid] == target:
                return True
            if target < row[mid]:
                r = mid - 1
            else:
                l = mid + 1
        return False