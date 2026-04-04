testCases = int(input())

for _ in range(testCases):
    n = int(input())
    nums = list(map(int, input().split()))
    tests = n//2
    flag = True

    for test in range(2, tests+1):
        for i in range(n):
            if i % test == 0:
                if nums[i]%test == 0:
                    print("NO")
                    flag = False
                    break
            else:
                if nums[i]%test != 0:
                    print("NO")
                    flag = False
                    break
    if flag:
        print("YES")
    
    
    