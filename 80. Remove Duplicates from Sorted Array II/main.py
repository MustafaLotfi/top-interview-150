class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 0
        k = len(nums)
        while i < (len(nums)-2):
            if nums[i] <= nums[i+1]:
                if (nums[i] == nums[i+1]) and (nums[i] == nums[i+2]):
                    if (i+3) == len(nums):
                        nums.pop(i+2)
                        k -= 1
                        break
                    else:
                        nums[i+2:k] = nums[i+3:k+1]
                        k -= 1
                elif nums[i] == nums[i+1]:
                    i += 2
                else:
                    i += 1
            else:
                break