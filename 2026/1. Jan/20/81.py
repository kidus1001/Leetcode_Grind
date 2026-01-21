class Solution(object):
    def search(self, nums, target):
        for i in nums:
            if i == target:
                return True
        return False
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """

#Note - Binary Search