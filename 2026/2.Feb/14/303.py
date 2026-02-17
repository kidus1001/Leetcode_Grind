class NumArray(object):

    def __init__(self, nums):
        for i in range(1,len(nums)):
            nums[i] += nums[i-1]
        self.nums = nums
        
        """
        :type nums: List[int]
        """
        

    def sumRange(self, left, right):
        if left == 0:
            return self.nums[right]
        else:
            return self.nums[right] - self.nums[left-1]
        """
        :type left: int
        :type right: int
        :rtype: int
        """
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)