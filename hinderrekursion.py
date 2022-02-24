# Programmet kontrollerar att den rekursiva formeln för hindertal gäller

# n! importeras
from math import factorial as fac

# n över k (binomialtal) importeras
from math import comb as over

# Catalantal definieras (C_n)
def cat(n):
	return int(1/(n+1)*over(2*n, n))

# Explicit formel för hindertal
def hinder(n):
	return cat(n) - (n-1)**2

# Rekursiv formel för hindertal
def rec(n):
	if n == 1: return 1
	else:
		recu = 1
		for i in range(2,n+1):
			recu = recu + cat(i) - cat(i-1) - 2*i + 3
	return recu

# Input m
m = int(input("m = "))

# Kontrollerar att den rekursiva formeln överensstämmer med den explicita formeln för varje heltal n, 1 <= n <= m (där m är inmatningen)
for i in range(1,m):
	if hinder(i) - rec(i) != 0: print(i, hinder(i), rec(i))
print("Done")