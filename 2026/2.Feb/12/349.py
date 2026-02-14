class Solution(object):
    def intersection(self, nums1, nums2):
        num1Hash = {}
        num2Hash = {}
        for num in nums1:
            num1Hash[num] = num1Hash.get(num, 0) + 1
        for num in nums2:
            num2Hash[num] = num2Hash.get(num, 0) + 1
        
        ans = []
        for k, v in num1Hash.items():
            if num1Hash[k] > 0 and num2Hash.get(k, 0) > 0:
                ans.append(k)
        return list(set(ans))
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        