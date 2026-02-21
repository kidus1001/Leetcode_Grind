t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    a = sorted(set(a))

    best = 0
    current = 1

    for i in range(1, len(a)):
        if a[i] - a[i - 1] == 1:
            current += 1
        else:
            best = max(best, current)
            current = 1

    best = max(best, current)
    print(best)