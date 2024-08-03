class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        lb = 0
        for j in range(n):
            if m > 0:
                found_index = False
                for i in range(lb, m):
                    if nums2[j] <= nums1[i]:
                        nums1[i+1:] = nums1[i:-1]
                        nums1[i] = nums2[j]
                        found_index = True
                    elif i == (m-1):
                        nums1[i+1] = nums2[j]
                        found_index = True
                    if found_index:
                        lb = i+1
                        m += 1
                        break
            else:
                nums1[j] = nums2[j]
        
            