testCases = int(input())

for _ in range(testCases):
    adj = 0
    n = int(input())
    state = []
    oneCount = 0
    strState = input()
    for i in range(n-1):
        num = int(strState[i])
        if num == 1:
            oneCount+=1
            if strState[i+1] == 1:
                adj+=1
        state.append(num)
    if strState[n-1] == "1":
        oneCount+=1
        
    if oneCount%2 == 0 and adj%2 == 0:
        print("YES")
    else:
        print("NO")
