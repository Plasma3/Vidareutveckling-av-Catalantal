from math import comb, factorial as fact
from sys import setrecursionlimit
setrecursionlimit(10000)

def cat_n(n:int): return comb(2 * n, n) // (n + 1)
def formel(n:int):
    out = 0
    for q in range(n):
        out += cat_n(q) * cat_n(n - q)
    return out

N = 0
DP = []

def enkel_överkors_dfs(x:int, y:int, crossed:int):
    if x == y and x == N: return 1

    if DP[x][y][crossed] != -1: return DP[x][y][crossed]

    out = 0
    if crossed == 1:
        if y < N:
            out += enkel_överkors_dfs(x, y + 1, 1)
        if x < N and x < y:
            out += enkel_överkors_dfs(x + 1, y, 1)
    else:
        if x < N: 
            out += enkel_överkors_dfs(x + 1, y, 0)
        if y < N and y < x:
            out += enkel_överkors_dfs(x, y + 1, 0)
        if crossed == 0 and y == x:
            out += enkel_överkors_dfs(x, y + 1, 1)
    
    DP[x][y][crossed] = out
    return out

for n in range(1, 1000 + 1):
    N = n
    DP = [[[-1, -1] for _ in range(n + 1)] for _ in range(n + 1)]

    f, b = formel(N), enkel_överkors_dfs(0, 0, 0) - cat_n(n)

    print("===", "n =", n, "===")
    if f != b: print("n:" + str(n), str(f), "!=", str(b))
