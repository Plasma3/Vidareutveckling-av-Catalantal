# Programmet användes för att få fram en indikation om gränsvärdet för hindertalen

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

# Input m
m = int(input("m = "))

# Jämför kvoten mellan det n:te hinder-talet och det (n+1):te hinder-talet, för n upp till och med inmatat m-värde
# och visar var funktionen inte är växande
count = 0
minskning = []
for n in range(1,m+1):
    print("n+1 =", n+1, "n =", n, "Kvot =", hinder(n+1)/hinder(n))
    if n >= 2:
        if hinder(n+1)/hinder(n) < hinder(n)/hinder(n-1):
            print("Minskning vid n =", n+1)
            count = count + 1
            minskning.append(n+1)
print("Minskning vid", count, "ställen", minskning)
# Kvoten verkar gå mot 4 när n går mot oändligheten