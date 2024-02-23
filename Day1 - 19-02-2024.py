#P1
-------------------
a = int(input())
b = int(input())
if a > b:
    print(a)
else:
    print(b)
    
#P2
--------------------
a=int(input())
b=int(input())
c=int(input())
if a>b and b>c:
    a=0
elif b>c:
    b=0
else:
    c=0
if a>b and b>c:
    print(a)
elif b>c:
    print(b)
else:
    print(c)

#P3
----------------------
a = int(input())
b = int(input())
if a > b:
    print(b)
else:
    print(a)

#P4
-----------------------
a = int(input())
b = int(input())
c = int(input())
if a>b and a>c:
    a=0
elif b>c:
    b=0
else:
    c=0
if a>b and a>c:
    print(a)
elif b>c:
    print(b)
else:
    print(c)
    
#P5
-----------------------
for i in range (100):
    print("Hello World")

#P6
-------------------------
a,b=map(int,input().split())
if a>b:
    print("a > b")
elif a==b:
    print("a == b")
else:
    print("a < b")

    
#P7
---------------------------
a,b,c=map(int,input().split())
if a+b >c:
    print("Yes")
elif a+c >b:
    print("Yes")
elif c+b >a:
    print("Yes")
else:
    print("No")

#P8 number reverse
-------------------------
n=int(input())
if n>0:
    rev=0
    while n!=0:
        d=n%10
        rev=rev*10+d
        n=n//10
    print(rev)
elif n==0:
    print(n)
else:
    res=0
    n=n*-1
    while n!=0:
        d=n%10
        rev=rev*10+d
        n=n//10
    print(-1*rev)

#P9 water melon
#Approach - 1
------------------------
w = int(input())
if w>2 and w%2==0:
    print("Yes")
else:
    print("No")

#Approach - 2
-----------------------
w = int(input())
if w%2==0:
    if w > 2:
        print("Yes")
    else:
        print("No")
else:
    print("No")
    
#P10 fever
#Appraoch - 1
--------------------
t = int(input())
for i in range(t):
    n = int(input())
    if n > 98:
        print("Yes")
    else:
        print("No")

#Appraoch - 2
-----------------------
t=int(input())
i=1
while :
    x=int(input())
    if(x>98):
        print("Yes")
    else:
        print("No")
    i=i-1
    
#P11 discount
------------------------
t=int(input())
for i in range (t):
    d=int(input())
    print(100-d)

#P12  discount of 2 tvs
-------------------------------
t=int(input())
while(t>0):
    w,x,y,z=map(int,input().split())
    if w-y > x-z:
        print("Second")
    elif w-y < x-z:
        print("First")
    else:
        print("Any")
    t=t-1

#P13 candy
---------------------
k=int(input())
for i in range (k):
    p,r=map(int,input().split())
    if p>r:
        k=p-r
        if k%4==0:
            print(k//4)
        else:
            print((k//4)+1)
    else:
        print(0)
        
#P14
#Approach - 1
-----------------------------
k=int(input())
for i in range (k):
    p,r=map(int,input().split())
    k=p*r
    if k%4==0:
        print(k//4)
    else:
        print((k//4)+1)

#Approach - 2
---------------------------------
k=int(input())
while k!=0:
    p,r=map(int,input().split())
    k=p*r
    if k%4==0:
        print(k//4)
    else:
        print((k//4)+1)
    k=k-1

#Approach - 3
-----------------------------
k=int(input())
while k!=0:
    p,r=map(int,input().split())
    ts=p*r
    tp=0
    while ts>=4:
        tp=tp+1
        ts=ts-4
    if tp==0:
        print(tp)
    else:
        print(tp+1)


    


