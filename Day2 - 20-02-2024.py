#P1 profit of n glasses
#Approach-1
--------------------------
t = int(input())
for i in range(t):
    n = int(input())
    x = int((n*50) - ((0.7)*(n*50)))
    print(x)

#Approach-2
--------------------------
t = int(input())
while t > 0:
    n = int(input())
    x = int((n*50) - ((0.7)*(n*50)))
    print(x)
    t = t - 1

#Approach-3
------------------------
t = int(input())
def test(t):
    if t > 0:
        n = int(input())
        x = int((n*50) - ((0.7)*(n*50)))
        print(x)
    else:
        return
    test(t-1)
test(t)

#Approach - 4
---------------------------
t = int(input())
def profit(n):
    x = int((n*50) - ((0.7)*(n*50)))
    return x
def test(t):
    if t > 0:
        n = int(input())
        print(profit(n))
    else:
        return
    test(t-1)
test(t)
    
#P2 watching movies at 2x
#Approach - 1
----------------------------------
x,y=map(int,input().split())
def min(x,y):
    rem=x-(y//2)
    print(rem)
min(x,y)

#Approach - 2
-------------------------------
x,y=map(int,input().split())
print(((x-y)+(y//2)))

#Approach - 3
--------------------------------
x,y=map(int,input().split())
def min(x,y):
    print(((x-y)+(y//2)))
min(x,y)

#P3 lucky four
#Approach-1
----------------------------
t=int(input())
def integer(n):
    c=0
    while n>0:
        if n%10==4:
            c=c+1
        n=n//10
    return c
def test(t):
    for n in range (t):
        n=int(input())
        m=integer(n)
        print(m)
    test(t-1)
test(t)

#Approach-2
-------------------------
t=int(input())
for i range (t):
    n=int(input())
    c=0
while n>0:
    if n%10==4:
        c=c+1
    n=n//10
print(c)

#Approach-3
--------------------------
t=int(input())
def integer(n):
    c=0
    while n>0:
        if n%10==4:
            c=c+1
        n=n//10
    return c
def test(t):
    n=int(input())
    m=integer(n)
    print(m)
    test(t-1)
test(t)

#P4
#Approach - 1
-----------------------------
t = int(input())
for i in range(t):
    n = int(input())
    c = 0
    while n > 0:
        if n%10 == 4:
            c = c + 1
        n = n // 10
    print(c)

#Appraoch - 2
----------------------------------
def test(n):
    if t == 0:
        return
    else:
        n = int(input())
        print(count(n))
    test(n-1)
def count(n):
    c = 0
    while n > 0:
        r = n%10
        if r == 4:
            c = c + 1
        n = n // 10
    return c
t = int(input())
test(t)

#P5 compute N! fact
#Approach-1
--------------------------
N=int(input())
def fac(N):
        if N==0:
            return 1
        else:
            return N*(fac(N-1))
result=fac(N)
print(result)

#Approach-2
-------------------------------
N=int(input())
def fac(N):
        if N!=0:
            return N*(fac(N-1))
        else:
            return 1
result=fac(N)
print(result)
#Approach-3
------------------------------
n = int(input())
r = 1
for i in range(1,n+1):
    r = r * i
print(r)

#P6
-----------------------
n = int(input())
if n%2==0:
    print(n+2)
else:
    print(n+1)

#P7 append 3
#Approach-1
--------------------
n=int(input())
x=n/1000
y=x+3
z=y*1000
print((z*10)+3)

#Approach-2
--------------------
n=int(input())
def temp(n):
    r=n
    c=0
    while r>0:
        c+=1
        r=r//10
    n=(3*pow(10,c))+n
    n=n*10+3
    return n
print(temp(n))

