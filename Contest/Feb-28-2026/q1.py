testCases = int(input())
for _ in range(testCases):
    distances = list(map(int, input().split()))
    timur = distances[0]
    ans = 0
    for i in range(1, len(distances)):
        if distances[i] > timur:
            ans += 1
    print(ans)