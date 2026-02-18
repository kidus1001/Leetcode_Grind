#Using prefix / postfix
class Solution(object):
    def productExceptSelf(self, nums):
        n = len(nums)

        prefix = [1]*(n+1)
        postfix = [1]*(n+1)

        for i in range(n):
            prefix[i] = prefix[i-1]*nums[i]
        

        for i in range(n-1, -1, -1):
            postfix[i] = postfix[i+1] * nums[i]

        ans = [0]*n
        ans[0] = postfix[1]

        for i in range(1, n):
            ans[i] = prefix[i-1]*postfix[i+1]
        return ans
    
    
    
    
# class Solution(object):
#     def productExceptSelf(self, nums):
#         allProduct = 1
#         zeroCount = 0
#         for num in nums:
#             if num != 0:
#                 allProduct *= num
#             else:
#                 zeroCount += 1
        
#         for i in range(len(nums)):
#             if nums[i]!=0:
#                 if zeroCount==0:
#                     nums[i] = allProduct/nums[i]
#                 else:
#                     nums[i] = 0
#             else:
#                 if zeroCount == 1:
#                     nums[i] = allProduct
#                 else:
#                     nums[i] = 0
#         return nums

#         """
#         :type nums: List[int]
#         :rtype: List[int]
#         """
        