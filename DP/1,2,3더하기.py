T = int(input())

for _ in range(T):
    n = int(input())

    dp = [1 for _ in range(n + 1)]

    if n >= 2:
        dp[2] = 2
    if n >= 3:
        dp[3] = 4

    if n >= 4:
        for i in range(4, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3]

    print(dp[n])
