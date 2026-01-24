#Incorrect Solution

testCases = int(input())
for _ in range(testCases):
    a, b = map(int, input().split())
    if a == 0 and b == 0:
        print("YES")
    else:
        if a == b:
            print("NO")
        else:
            print("YES")