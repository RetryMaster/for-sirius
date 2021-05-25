# 2.1

a = int(input())
b = a*2+1
c = a-1
s = b+2*a+c*2
while c > 0:
    c = c-1
    s = s+2*c
print(s)

# 2.2

n = int(input())
k = 1
s = 0
s+=k+2*n
while n!=0:
    s+=n*2
    n-=1
print(s)


# 4

a = int(input())
b = int(input())
c = int(input())
d = int(input())
k = 0
A = []
m = 2**a+2**b-2**c
while m//2!=1:
    l = m % 2
    A.append(l)
    m = m//2
A.append(1)
print (A)
for i in range (len(A)):
    if A[i]==d:
        k+=1
print (k)

# 3
K = int(input())
M = int(input())
A = int(input())
B = int(input())
S = 0
L = 0
while A <= B:
    if A % K == 0:
        S += 1
    if A % M == 0:
        L += 1
    A += 1
D = S-K
print(D)

# 3.1
K = int(input())
M = int(input())
A = int(input())
B = int(input())
S = 0
L = 0
D = 0
if B>=A:
    while A <= B:
        if A % K == 0:
            S += 1
        if A % M == 0:
            L += 1
        A += 1
if A>B:
    while B <= A:
        if B % K == 0:
            S += 1
        if B % M == 0:
            L += 1
        B += 1
D = S-L
print(D)


# 3.2
K = int(input())
M = int(input())
A = int(input())
B = int(input())
m = 0
k = 0
for i in range(B-A+1):
    if A % K == 0:
        k+=1
    if A % M == 0:
        m+=1
    A+=1
print (k-m)



# 1
a = int(input())
b = int(input())
c = int(input())
w = 0
while c - 3*a - 2*b >= 0:
    # if c - 3*a - 2*b >= 0:
    c = c-3*a-2*b
    w+=1
print(w)