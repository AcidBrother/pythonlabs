'''
#6.1
import time
n=int(input())
for i in range(n, 0, -1):
    print('Осталось %d секунд' % i)
    time.sleep(1)
print('Пуск!!!')
'''
'''
#6.2
n=int(input())-1
c=1
while n>-1:
        print(' '*n + '*'*c) #Я ЧЕСТНО НЕ ЗНАЛ ЧТО В ПИТОНЕ МОЖНО УМНОЖАТЬ КОЛИЧЕСТВО СИМВОЛОВ
        c += 2
        n -= 1
'''
'''
#6.3
n=[0]*17
for i in range(0,len(n)):
    n[i]=int(input())
for i in range(0,len(n)):
    if i%n[i]==0:
        print("ДА")
    else:
        print("НЕТ")
'''
'''
#6.4
n=int(input())
s=0
for i in range(0,n):
    a=int(input())
    if i==0:
        s+=a
        print(0)
    else:
        s+=a
        if a>(s/(i+1)):
            print('>')
        elif a<(s/(i+1)):
            print('<')
        else:
            print('0')
'''
'''
#6.5
n=int(input())
s=0
for i in range(0,n):
    a=int(input())
    b=int(input())
    s=s+a/b

num=0
k =  1

for i in range(int(input())):

   a, b = int(input()), int(input())

   num = num * b + a * k

   k *= b

x, y = num, k

while y > 0:

   x, y = y, x % y

print(num // x, '/', k // x)
'''
#6.6
n = int(input())
a = 0
p = 3.141592653589793
for i in range(0,n):
    a=a+(1/((i+1) ** 2))
print((p**2)/a)
'''
#6.7
n=int(input())
s=0
if n>0:
    for i in range(1,n+1):
        a=int(input())
        if i%2==0:
            s-=a
        else:
            s+=a
    print(s)
'''
