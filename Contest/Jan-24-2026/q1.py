testCases = int(input())

for _ in range(testCases):
    k, last = map(int, input().split())
    
    for i in range(k):
        last = last*2
    print (last)
    