# n! definieras
def fac(n):
    fact = 1
    for i in range(1,n+1):
        fact = fact * i
    return fact

# n över k (binomialtal) definieras
def over(n, k):
    return int(fac(n)/(fac(k)*(fac(n-k))))

# Catalantal definieras (C_n)
def cat(n):
    return int(1/(n+1)*over(2*n, n))

# Förskjuten diagonal-talen definieras
def fdiagonal(n, g):
    return int(over(2*n, n)) - int(over(2*n, n-1-g))

# Input, m
m = int(input("m = "))

# För n-värden fr.o.m. 1 t.o.m. det m-värdet som matades in (input), tar kvoten mellan det (n+1):a f-diagonal-talet och det n:te f-diagonal-talet, g fixt till n-1 för varje n
for i in range(1,m+1):
    g = i-1
    print("n =", i, "n+1 =", i+1, "g =", g, "Kvot =", fdiagonal(i+1, g)/fdiagonal(i,g))
    # (Här undersöks huruvida kvoten någonsin blir mindre än föregående kvot eller om funktionen är växande)
    # if i > 1:
    #    if fdiagonal(i+1, g)/fdiagonal(i,g) <= fdiagonal(i-1+1, g-1)/fdiagonal(i-1,g):
    #        print("Ej ökning vid", i)
    #        break
# Kvoten verkar gå mot 4 när n går mot oändligheten
# Funktionen verkar vara växande
# Obs: g kan naturligtvis bytas ut mot ett annat heltal där 1 <= g <= n-1. Ger samma indikation om att kvoten går mot 4 när n går mot oändligheten.
