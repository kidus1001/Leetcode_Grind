testCases = int(input())
for _ in range(testCases):
    n = int(input())
    chars = input()
    ans = 1
    
    mx = 1
    cur = 1
    for i in range(1,n):
        if chars[i] == chars[i-1]:
            cur+=1
        else:
            mx = max(mx, cur)
            cur = 1
    mx = max(mx, cur)
    print (ans+mx)


# testCases = int(input())
# for _ in range(testCases):
#     n = int(input())
#     chars = input()
#     myArr = []
#     myArr.append(5)
#     for i in range(n):
#         if chars[i] == "<":
#             myArr.append(myArr[-1]+1)
#         else:
#             myArr.append(myArr[-1]-1)
#     print(len(set(myArr)))