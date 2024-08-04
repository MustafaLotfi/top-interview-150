class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        if k > len(nums):
            k %= len(nums)
        
        nums1 = nums[-k:]
        nums[k:] = nums[:-k]
        nums[:k] = nums1