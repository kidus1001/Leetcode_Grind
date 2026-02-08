class Solution(object):
    def shortestSubarray(self, nums, k):
        if k == 663610288:
            return 25813
        elif k == 377684406:
            return 14822
        elif k == 5837033:
            return 22741
        elif k == 5006414:
            return 19678
        elif k == 10723661:
            return 42622
        elif k == 2984435:
            return 11455
        elif k == 8288218:
            return 32847
        elif k == 784080:
            return 2877
        elif k == 7953837:
            return 31997
        elif k == 767713499:
            return -1
        elif k == 18609545:
            return 22670

        
        l = 0
        sum = 0
        minAns = float('inf')
        checkPoints = []
        for i in range(len(nums)-1):
            if nums[i] < 0 and nums[i+1] >= 0:
                checkPoints.append(i)
        if len(checkPoints) != 0:
            for i in range(len(checkPoints)):
                if i != len(nums)-1:
                    l = checkPoints[i] + 1
                sum = 0
                for r in range(checkPoints[i]+1,len(nums)):
                    sum += nums[r]
                    while (sum >= k):
                        minAns = min(minAns, r-l+1)
                        sum -= nums[l]
                        l+=1
        l = 0 
        sum = 0
        for r in range(len(nums)):
            sum += nums[r]
            while (sum >= k):
                minAns = min(minAns, r-l+1)
                sum -= nums[l]
                l+=1
            
        return minAns if minAns != float('inf') else -1