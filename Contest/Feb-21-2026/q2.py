# Got a hang of it, not done yet tho

n, q = map(int, input().split())

prices = list(map(int, input().split()))
prices.sort()
priceOri = prices
suffix = [0]*n 
suffix[n-1] = prices[n-1]
for i in range(n-2, -1, -1):
    suffix[i] = priceOri[i] + priceOri[i+1]

for i in range(1, n):
    prices[i] = prices[i] + prices[i-1]

print(prices)
print(suffix)
for _ in range(q):
    purchases, cheap = map(int, input().split())
    l = n-purchases
    r = n-1
    ans = 0
    if l > 0:
        ans = prices[n-1] - prices[l-1]
    else:
        ans = prices[n-1]
    
    print(ans)
    