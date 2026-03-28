import sys

input = sys.stdin.read
data = input().split()
idx = 0
t = int(data[idx]); idx += 1
out = []

for _ in range(t):
    n = int(data[idx]); idx += 1
    m = int(data[idx]); idx += 1
    req = [(0, 0)]  # start at 0 side 0
    for __ in range(n):
        a = int(data[idx]); idx += 1
        b = int(data[idx]); idx += 1
        req.append((a, b))
    
    total = 0
    for i in range(1, len(req)):
        prev_a, prev_b = req[i-1]
        curr_a, curr_b = req[i]
        diff = curr_a - prev_a
        if prev_b == curr_b:
            # need even runs
            max_runs = diff if diff % 2 == 0 else diff - 1
        else:
            # need odd runs
            max_runs = diff if diff % 2 == 1 else diff - 1
        total += max_runs
    
    # last interval
    last_a, last_b = req[-1]
    total += m - last_a
    
    out.append(str(total))

print("\n".join(out))