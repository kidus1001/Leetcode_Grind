testCases = int(input())

for i in range(testCases):
    n = int(input())
    nums = list(map(int, input().split()))
    
    sumN = sum(nums)
    
    if sumN % 2 == 0:
        print ("NO")
    else:
        print ("YES")