testCases = int(input())
 
for _ in range(testCases):
    n = int(input())
    arr = list(map(int, input().split()))
    if 67 in arr:
        print("YES")
    else:
        print("NO")