testCases = int (input())

for _ in range (testCases):
    n = int(input())
    nums = list(map(int, input().split()))
    if nums[0] == 0 and nums[-1] == 0:
        print("Bob")
    else:
        print("Alice")
    # oneCount, zeroCount = 0, 0 
    # for num in nums:
    #     if num == 1:
    #         oneCount += 1
    #     else:
    #         zeroCount += 1
    
    # if (oneCount / n ) >= 0.5:
    #     print("Alice")
    # else:
    #     print("Bob")
    
    # if zeroCount/n > 0.5:
    #     print("Bob")
    # else:
    #     print("Alice")