class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        pre = [1] * len(nums)
        for i in range(len(nums)):
            if i == 0:
                pre[i] = nums[i]
            else:
                pre[i] = pre[i-1] * nums[i]

        post = [1] * len(nums)
        for i in range(len(nums)-1, -1, -1):
            if i == len(nums)-1:
                post[i] = nums[i]
            else:
                post[i] = post[i+1] * nums[i]

        result = [1] * len(nums)
        for i in range(len(nums)):
            if i == 0:
                result[i] *= post[i+1]
            elif i == len(nums) - 1:
                result[i] *= pre[i-1]
            else:
                result[i] *= pre[i-1] * post[i+1]

        return result

# include, don't include
# take max non-zero

#      -1  0  1  2  3
# pre [-1]
# pre [-1, 0]
# pre [-1, 0, 0]
# pre [-1, 0, 0, 0]
# pre [-1, 0, 0, 0, 0]

#       -1  0  1  2  3
# post              [3]
# post           [6, 3]
# post        [6, 6, 3]
# post     [0, 6, 6, 3]
# post [-1, 0, 6, 6, 3]