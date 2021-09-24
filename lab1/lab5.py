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

#5.2
n=int(input())
a=1
c=0
while a!=n:
    if a*2==n:
        a*=2
        c+=1
        print(a,' ', c)
    elif a*2>n:
            while a!=n:
                a+=1
                c+=1
                print(c)
    else:
        a*=2
        c+=1
        print(a,' ', c)
print(c)
