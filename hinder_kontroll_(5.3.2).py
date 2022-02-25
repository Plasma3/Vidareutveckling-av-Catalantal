from math import comb, factorial as fact
from sys import setrecursionlimit
setrecursionlimit(10000)

def formel(n:int): return (comb(2 * n, n) // (n + 1)) - ((n - 1) * (n - 1))

N = 0
DP = []

def n_minus_1_dfs(x:int, y:int):
    if x == y and x == N: return 1
    if x == n - 1 and y == 1: return 0

    if DP[x][y] != -1: return DP[x][y]

    out = 0
    if x < N: 
        out += n_minus_1_dfs(x + 1, y)
    if y < N and y < x:
        out += n_minus_1_dfs(x, y + 1)
    
    DP[x][y] = out
    return out

for n in range(1000 + 1):
    N = n
    DP = [[-1 for _ in range(n + 1)] for _ in range(n + 1)]

    f, b = formel(N), n_minus_1_dfs(0, 0)

    print("===", "n =", n, "===")
    if f != b: print("n:" + str(n), str(f), "!=", str(b))
