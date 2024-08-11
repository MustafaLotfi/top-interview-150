class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        i = 0
        nums_len = len(nums)
        while i < nums_len:
            best_index_for_jumping = i
            last_index_could_reach = i
            j = i+1
            while (j < nums_len) and (j <= (i+nums[i])):
                if last_index_could_reach < j+nums[j]:
                    last_index_could_reach = j+nums[j]
                    best_index_for_jumping = j
                j += 1
            if i == (nums_len-1):
                return True
            elif i == best_index_for_jumping:
                return False
            else:
                i = best_index_for_jumping
        
        return True
                

print(Solution().canJump([2, 3, 1, 1, 4]))