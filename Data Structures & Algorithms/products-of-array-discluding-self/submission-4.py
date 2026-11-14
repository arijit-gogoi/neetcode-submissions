class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [1] * n
        left = right = 1
        
        for i in range(n):
            res[i] *= left
            res[~i] *= right
            left *= nums[i]
            right *= nums[~i]
        return res