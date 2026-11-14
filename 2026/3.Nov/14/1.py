class Solution(object):
    def twoSum(self, nums, target):
        hashNum = {}

        for i in range (len(nums)):
            otherNum = target - nums[i]
            if otherNum in hashNum:
                return ([i, hashNum[otherNum]])
            hashNum[nums[i]] = i
        