'''
#5.1
d=int(input())
m=int(input())
y=int(input())
if m>=3:
    m-=2
elif m==2:
    m=12
elif m==1:
    m=11
c=y//100
y%=100
print((d + ((13*m - 1) // 5 ) + y + (y //4 + c // 4 - 2*c + 777))%7)
'''
'''
#5.2
n = int(input())
c=0
while n!=1:
   if n%2 == 0:
       n/=2
       c+=1
   else:
       n -=1
       c += 1
print(c)
'''
'''
#5.3
a=int(input())
b=int(input())
    while ((a!=0) or (b!=0)):
    n=int(input())
    c=int(input())
    if n==1:
        a-=c
    elif n==2:
        b-=c
    print(a,' ',b)
'''

'''
#5.4
import random
a=int(input())
c=0
b=0
while a!=0:
    if(a>3):
        b=random.randint(1, 3)
    else:
        b=a
    if(a-b==0):
        print("You lose")
        break
    else:
        a-=b
        print(b,' ',a)
    c=int(input())
    if(a-c==0):
        print("You win")
        break
    else:
        a-=c
        print(c,' ',a)
'''
'''
#5.5
import random
a=int(input())
c=0
b=0
while a!=0:
    if(a>3):
        b=random.randint(1, 3)
    else:
        if a==3:
            b=2
        elif a==2:
            b=1
        else:
            b=1
    if(a-b==0):
        print("You win")
        break
    else:
        a-=b
        print(b,' ',a)
    c=int(input())
    if(a-c==0):
        print("You lose")
        break
    else:
        a-=c
        print(c,' ',a)
'''

#5.6
a=int(input())
b=int(input())
c=int(input())
while ((a!=0) or (b!=0) or (c!=0)):
    i=int(input())
    n=int(input())
    if i==1 and not(a-n<0) and not(n<0):
        a-=n
        print(a,' ',b,' ',c)
    elif i==2 and not(b-n<0) and not(n<0):
        b-=n
        print(a,' ',b,' ',c)
    elif i==3 and not(c-n<0) and not(n<0):
        c-=n
        print(a,' ',b,' ',c)
