t = int(input())


def solve(st, memo, x, y):
    if st in memo:
        return memo[st]

    if st == "pr":
        return x

    if st == "rp":
        return y

    if st.count("p") == 0 or st.count("r") == 0:
        return 0

    if len(st) <=1:
        return 0

    memo[st] = 0
    for i in range(len(st)):
        if st[i] == "p":
            if i+1<len(st) and st[i + 1] == "r":
                memo[st] = max(memo[st], solve(st[0:i]+st[i+2:], memo, x, y) + x)
        if st[i] == "r":
            if i+1<len(st) and st[i + 1] == "p":
                memo[st] = max(memo[st], solve(st[0:i]+st[i+2:], memo, x, y) + y)

    return memo[st]


for _ in range(t):
    st = input().strip()
    x, y = list(map(int, input().strip().split()))
    memo = {}
    print(solve(st, memo, x, y))
