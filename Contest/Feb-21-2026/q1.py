testCases = int(input())

for _ in range(testCases):
    n = int(input())
    arr = list(map(int, input().split()))
    maximum = max(arr)
    print(maximum*n)