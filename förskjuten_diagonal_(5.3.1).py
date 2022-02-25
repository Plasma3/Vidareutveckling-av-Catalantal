from math import comb, factorial as fact

def formel(n:int, g:int): return comb(2 * n, n) - comb(2 * n, n - 1 - g)

N, G = 0, 0
DP = []

def förskjuten_diagonal_dfs(x:int, y:int):
    if x == y and x == N: return 1

    if DP[x][y] != -1: return DP[x][y]

    out = 0
    if x < N: 
        out += förskjuten_diagonal_dfs(x + 1, y)
    if y < N and y < x + G:
        out += förskjuten_diagonal_dfs(x, y + 1)
    
    DP[x][y] = out
    return out

for n in range(100 + 1):
    print("===", "n =", n, "===")
    for g in range(n):
        N, G = n, g
        DP = [[-1 for _ in range(n + 1)] for _ in range(n + 1)]

        f, b = formel(N, G), förskjuten_diagonal_dfs(0, 0)

        if f != b: print("n:" + str(n), "g:" + str(g), str(f), "!=", str(b))
