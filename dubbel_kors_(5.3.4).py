from math import comb, factorial as fact
from sys import setrecursionlimit
setrecursionlimit(10000)

def cat_n(n:int): return comb(2 * n, n) // (n + 1)
def formel(n:int):
    out = 0
    for q in range(n-1):
        out += cat_n(q) * cat_n(n - q - 1)
    return out

N = 0
DP = []

def direkt_dubbellkors_dfs(x:int, y:int, crossed:int):
    if x == y and x == N: return 1

    if DP[x][y][crossed] != -1: return DP[x][y][crossed]

    out = 0
    if x < N: 
        out += direkt_dubbellkors_dfs(x + 1, y, crossed)
    if y < N and y < x:
        out += direkt_dubbellkors_dfs(x, y + 1, crossed)
    if crossed == 0 and y == x and x < N - 1:
        out += direkt_dubbellkors_dfs(x + 1, y + 1, 1)
    
    DP[x][y][crossed] = out
    return out

for n in range(1, 1000 + 1):
    # n = 5
    N = n
    DP = [[[-1, -1] for _ in range(n + 1)] for _ in range(n + 1)]

    f, b = formel(N), direkt_dubbellkors_dfs(0, 0, 0) - cat_n(n)

    print("===", "n =", n, "===")
    if f != b: print("n:" + str(n), str(f), "!=", str(b))
