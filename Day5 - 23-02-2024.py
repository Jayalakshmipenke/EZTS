#P1 odd even index
#Approach-1
---------------------------
s = input()
n = len(s)
es = ""
os = ""
for i in range(n):
    if i%2 == 0:
        es = es + s[i]
    else:
        os = os + s[i]
print(os+es)

#Approach-2
---------------------
s = input()
os = s[1::2]
es = s[::2]
print(os+es)

#Approach-3
------------------------
s=str(input())
print(s[1::2]+s[::2])

#P2 occurrence of a character
#Approach-1
----------------------------------
s=str(input())
ch=input()
count=0
s1=len(s)
for i in range (s1):
    if s[i]==ch:
        count=count+1
print(count)

#Approach-2
----------------------------------
s = input()
c = 0
ch = input()
for i in s:
    if i == ch:
        c = c + 1
print(c)

#Approach - 3
------------------------------
s = input()
ch = input()
print(s.count(ch))

#P3count of char in string consider only even index
#Approach - 1
---------------------------------------
s=str(input())
ch=input()
count=0
for i in range (len(s)):
    if i%2==0:
        if s[i]==ch:
            count=count+1
print(count)

#Approach - 2
--------------------------------
s = input()
c = 0
ch = input()
for i in range(len(s)):
    if s[i] == ch and i%2==0:
        c = c + 1
print(c)

#Approach - 3
--------------------------------
s = input()
ch = input()
x = s[::2]
print(x.count(ch))

#P4 vowels in a string
#Approach-1 & #Approach-2
---------------------------------------
s=input()
c=0
v=['a','e','i','o','u','A','E','I','0','U']  #v="aeiouAEIOU"
for i in range (len(s)):
    if s[i] in v:  #IF I NOT IN V:
        c=c+1
    else:#optional
        break
if c!=0: #c==0
    print("Yes")
else:
    print("No")
    
#Approach-3
------------------------------------
s = input()
v = "aeiouAEIOU"
for i in s:
    if i not in v:
        print("No")
        break
else:
    print("Yes")

#P5 digits in a string
#Approach-1
------------------------------
s=input()
d="1234567890"
c=0
for i in range (len(s)):
    if s[i] in d:
        c=c+1
if c==len(s):
    print("Yes")
else:
    print("No")

#Approach - 2
s = input()
d = "0123456789"
c = 0
for i in s:
    if i not in d:
        c = c + 1
if c == 0:
    print("Yes")
else:
    print("No")
    
#Approach-3
----------------------------
s=input()
d="1234567890"
c=0
for i in s:
    if i not in d:
        print("No")
        break
else:
    print("Yes")

#Approach-4
------------------------------
s = input()
if s.isdigit():
    print("Yes")
else:
    print("No")

#P6 count vowels and consonant
#Approach-1
------------------------------------
s=input()
v="aeiouAEIOU"
c="BCDFGHJKLMNPQRSTVWXYZbcdfghjklmnpqrstvwxyz"
cv=0
cc=0
for i in s:
    if i in v:
        cv=cv+1
    else:
        if i in c:
            cc=cc+1
print(cv,cc)

#Approach-2
-----------------------------------------
s=input()
v="aeiou"
c="bcdfghjklmnpqrstvwxyz"
s=s.lower()
cv=0
cc=0
for i in s:
    if i in v:
        cv=cv+1
    else:
        if i in c:
            cc=cc+1
print(cv,cc)

#Approach-3
---------------------------------------
s=input()
v="aeiouAEIOU"
cv=0
cc=0
for i in s:
    if i.isalpha():
        if i in v:
            cv=cv+1
        else:
            cc=cc+1
print(cv,cc)     


#P7
#Approach-1
-----------------------------------
s=input()
r=""
i=1
for i in range (len(s)):
    c=1
    if i!=i:
        break
    else:
        c=c+1
    r=r+c
print(r)

#Approach-2
---------------------------------
s = input()
c = 1
r = ""
for i in range(1,len(s)):
    if s[i] == s[i-1]:
        c = c + 1
    else:
        r = r + s[i-1]
        r = r + str(c)
        c = 1
r = r + s[len(s)-1] + str(c)
print(r)

#P8 word count,vowel count and consonent count
#Approach-1
-------------------------------------
t=int(input())
v="aeiou"
for i in range (t):
    s=list(input().split())
    vc=0
    cc=0
    wc=len(s)
    for j in s:
        for k in j:
            if k.isalpha():
                if k in v:
                    vc=vc+1
                else:
                    cc=cc+1
    print(wc,vc,cc)

#Approach - 2
-------------------------------------
t = int(input())
v = "aeiou"
for i in range(t):
    s = input()
    vc = 0
    cc = 0
    for j in s:
        if j.isalpha():
            if j in v:
                vc = vc + 1
            else:
                cc = cc + 1
    wc = len(s.split())
    print(wc,vc,cc)

#P9 guess the problem-1
---------------------------
t=int(input())
for i in range t:
    s1,s2=input().split()
    r=""
    for j in s2:
        if j not in s1:
            r=r+j
    print(r)


#P10
--------------------------
t = int(input())
for i in range(t):
    a,b = input().split()
    b = int(b)
    r = ""
    for i in a:
        k = ord(i)+b
        if k > 122:
            k = 96 + (k-122)
            r = r + chr(k)
        else:
            r = r + chr(k)
    print(r)


#OOPS
#P11
------------------------------
class cse:
    def hello(self):
        print("Hello cse")
class aiml:
    def hello(self):
        print("Hello aiml")
ob1=cse()
ob1.hello()

#P12
--------------------------------------
class classa:
    def factorial(self,n):
        r = 1
        for i in range(1,n+1):
            r = r * i
        print(r)
ob = classa()
ob.factorial(5)

#P13
-------------------------------
class a:
    def __init__(self):
        print("Hello")
    def hello(self):
        print("Hello a")
ob = a()

#P14
----------------------------------
class classa:
    def __init__(self,n):
        self.n = n
        print(n)
    def factorial(self):
        r = 1
        for i in range(1,self.n+1):
            r = r * i
        print(r)
ob = classa(5)
ob.factorial()

#P15
--------------------------
class classa:
    def __init__(self,n):
        self.n = n
    def factorial(self):
        print(self.fact(self.n))
    def fact(self,n):
        if n == 1:
            return 1
        else:
            return n * self.fact(n-1)
ob = classa(5)
ob.factorial()

























