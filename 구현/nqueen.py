def check(x):
    for i in range(x):
        if row[x] == row[i]:
            return False
        if abs(row[x] - row[i]) == x - i:
            return False

    return True


def dfs(x):
    global result

    if x == n:
        result += 1
    else:
        for i in range(n):
            row[x] = i
            if check(x):
                dfs(x + 1)


n = int(input())
result = 0
row = [0] * n
dfs(0)
print(result)
