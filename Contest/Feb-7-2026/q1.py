testCases = int(input())

for _ in range(testCases):
    n = int(input())
    arr = list(map(int, input().split()))
    
    maxIndex = 0
    lenArr = []
    for i in range(n-1):
        lenArr.append(abs(arr[i] - arr[i+1]))
        if lenArr[i] > lenArr[maxIndex]:
            maxIndex = i
    
    ans = sum(lenArr)
    if maxIndex != n-2 and maxIndex != 0:
        ans -= lenArr[maxIndex]
        ans -= lenArr[maxIndex-1]
        ans += abs(lenArr[maxIndex] - lenArr[maxIndex-1])
    elif maxIndex == 0:
        ans -= lenArr[0]
    else:
        ans -= lenArr[n-2]
    print (ans)








# testCases = int(input())

# for _ in range(testCases):
#     n = int(input())
#     arr = list(map(int, input().split()))
    
#     maxIndex = 0
#     for i in range(n):
#         if arr[i] > arr[maxIndex]:
#             maxIndex = i
    
#     arr.remove(arr[maxIndex])
    
#     ans = 0
#     for i in range(n-2):
#         ans += abs(arr[i] - arr[i+1])
        
#     print(ans)