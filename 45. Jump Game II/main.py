class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        nums_len = len(nums)
        if nums_len == 1:
            return 0
        i = 0
        n_jump = 0
        while i < nums_len:
            best_index_for_jumping = i
            last_index_could_reach = i
            j = i+1
            while (j < nums_len) and (j <= (i+nums[i])):
                if last_index_could_reach < j+nums[j]:
                    last_index_could_reach = j+nums[j]
                    best_index_for_jumping = j
                j += 1

            n_jump += 1
            if (j) >= (nums_len) or (i >= (nums_len-1)):
                return n_jump
            else:
                i = best_index_for_jumping
            
                