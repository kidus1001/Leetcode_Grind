#Incomplete

testCases = int(input())

for _ in range(testCases):
    n = int(input())
    nums = list(map(int, input().split()))
    pair = True
    pairCheck = {}
    for num in nums:
        if pairCheck[num]:
            pairCheck[num] += 1
        else:
            pairCheck[num] = 1
    
    for k, v in pairCheck.items():
        if v%2 == 0:
            pair = False
            n -= v//2
    if sum(nums) % 2 == 0:
        if pair:
            print("NO")
        else:
            print("YES")