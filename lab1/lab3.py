'''
#3.1
a = input()

if float(a)>0:
    print('+')
elif float(a)==0:
    print('0')
elif float(a)<0:
    print('-')
'''

'''
#3.2
a = float(input())
b = float(input())
c = input()
if c== '+':
    print(a+b)
elif c=='':
    print(ab)
elif c=='-':
    print(a-b)
elif c=='/' and b!=0:
    print(a/b)
else:
    print("88888")
'''

'''
#3.3
a = int(input())
if (a/4 and a%4==0 and a/100!=0) or (a%400==0):
    print("Високосный")
else:print("Не високосный")
'''

'''
#3.4
a = int(input())
if a%2==0:
    print("Четное")
elif a%2!=0:
    print("Нечетное")
'''

'''
#3.5
a = input()
print(len(a)*2+3)
'''

'''
#3.6
a = int(input())
if a%10!=a//100 and  a%10!=a//10%10 and a//100!=a//10%10:
    print("ок")
    print(a%10, a//10%10, a//100)
elif (a%10==a//100 and  a%10!=a//10%10 and a//100!=a//10%10) or (a%10!=a//100 and  a%10==a//10%10 and a//100!=a//10%10) or (a%10!=a//100 and  a%10!=a//10%10 and a//100==a//10%10):
    print("В числе две одинаковые цифры")
elif ((a%10==a//100 and  a%10==a//10%10 and a//100==a//10%10)):
    print("В числе все цифры одинаковы")
'''

'''
#3.7
a = int(input())
i=0
b=10
bb=-1
c=-1
cc=-1
d=a
dd=a
for i in range(3):
    if a%10>c:
        c=a%10
        cc=i
    if a%10<b:
        b=a%10
        bb=i
    a//=10


for i in range(3):
    if cc!=i and bb!=i:
        dd=i

d = str(d)
for i in range(3):
    if dd==i:
        g=int(d[i])

if (b+c)/2 ==g:
    print("Вы ввели красивое число")
else:
    print("Жаль, вы ввели обычное число")
'''

'''
#3.8
a = int(input())
print(a%10)
print(a//10%10)
print(a//100)

b= a//100 + a//10%10
c = a//10%10 + a%10
if (b>c):
    d = str(b)+str(c)
    print(d)
else:
    d = str(c)+str(b)
    print(d)
'''

'''
#3.9
a = input()
b = float(40 * len(a))
print(b,"\n")
v = int(b//100)
vv = int(b%100)
print(v," р. ",vv, " коп.")
'''
