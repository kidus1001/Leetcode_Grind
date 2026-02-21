n = int(input())

episodes = list(map(int, input().split()))
sumTotal = sum(episodes)

total = (n * (n+1))//2
print(total-sumTotal)