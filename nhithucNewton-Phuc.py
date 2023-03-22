def binomialCoef(n, k): #tính tổ hợp nCk
    C = [0 for x in range(k+1)]
    C[0] = 1
    for i in range(n+1): 
        for j in range(min(i, k),0,-1):
            C[j] = C[j] + C[j-1]
    return C[k]
def nhithucnewton(a,b,n): #tính nhị thức (a+b)^n
    c=0
    k=0
    while(k!=n):
        c=c+binomialCoef(n, k)*(a**(n-k))*(b**k)
        k=k+1
    c=c+binomialCoef(n, k)*(a**(n-k))*(b**k)
    return c
# Input nhithucnewton(a,b,n) // (a+b)^n:
print(nhithucnewton(14,9,2))