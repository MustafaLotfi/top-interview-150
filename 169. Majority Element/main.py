class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        existance = {}
        for num in nums:
            if num not in existance.keys():
                existance[num] = 1
            else:
                existance[num] += 1
        
        most = 0
        for num in existance.keys():
            if existance[num] > most:
                majority = num
                most = existance[num]
        
        return majority
        