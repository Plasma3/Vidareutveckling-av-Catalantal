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

# Input, n
n = int(input("n = "))

g = 1

# Printar lista med f-diagonal-talet, Catalantalet och differensen t.o.m. n man matar in
for n in range(g,n+1):
    print("n =", n, "Diagonal:", fdiagonal(n, g), "Catalantal:", cat(n+1), "Differens:", fdiagonal(n, g) - cat(n+1))
    if fdiagonal(n, g) - cat(n+1) != 0:
        print("Fel vid n =", n)
# Programmet klarar upp
