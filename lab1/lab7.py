'''
#7.1
n=int(input())
a=''
t=True
for i in range(0,n):
    a=input()
    if ("Кот" in a) or ("кот" in a):
        t=False
if t:
    print("НЕТ")
else:
    print("Мяу")
'''
'''
#7.2
a=''
t=b=True
c=i=0
while b:
    i+=1
    a=input()
    if "СТОП" in a:
        b=False
    if ("Кот" in a) or ("кот" in a):
        t=False
        if c==0:
            c=i
if t:
    print(-1)
else:
    print(c)
'''

'''
#7.3
n=int(input())
a=''
t=True
for i in range(0,n):
    a=input()
    if ("Кот" in a) or ("кот" in a):
        t=False
        print("Мяу")
        break
if t:
    print("НЕТ")
'''
'''
#7.4
a=''
t=b=True
i=0
while b:
    i+=1
    a=input()
    if "СТОП" in a:
        b=False
    if ("Кот" in a) or ("кот" in a):
        t=False
        print(i)
        break
if t:
    print(-1)
'''
'''
#7.5
a=''
t=b=True
c=i=d=0
while b:
    i+=1
    a=input()
    if "СТОП" in a:
        b=False
    if ("Кот" in a) or ("кот" in a):
        t=False
        d+=1
        if c==0:
            c=i
if t:
    print(d,' ',-1)
else:
    print(d,' ',c)
'''
'''
#4.7
x = int(input())
y = int(input())
i=j=l=k=0
m=0
t=True
N=["север","восток","юг","запад"]
n="север"
a=''
while a!="стоп":
    a=input()
    if a=="юг":
        b=int(input())
        j-=b
        l+=1
    elif a=="север":
        b=int(input())
        j+=b
        l+=1
    elif a=="запад":
        b=int(input())
        i-=b
        l+=1
    elif a=="восток":
        b=int(input())
        i+=b
        l+=1
    if j==y and i==x and t:
        t=False
        k=l
print('')
print(k)
'''
'''
#7.7
n=int(input())
a=''
t=True
for i in range(0,n):
    a=input()
    if ("Кот" in a) or ("кот" in a):
        t=False
    if ("Пёс" in a) or ("пёс" in a):
        t=True
if t:
    print("НЕТ")
else:
    print("Мяу")
'''
'''
#7.8
n=int(input())
i=0
b=1
while n>0:
    a=input()
    if a == "раз" and b==1:
        i+=1
        b+=1
    elif a == "два" and b==2:
        i+=1
        b+=1
    elif a == "три" and b==3:
        i+=1
        b+=1
    elif a == "четыре" and b==4:
        i+=1
        b=1
    else:
        print("Правильных отсчётов было ",i,", но теперь вы ошиблись.")
        i=0
        b=1
        n-=1
        if not(n>0):
            print("На сегодня хватит.")
            break
'''
'''
#7.9
a=''
list=[]
b=i=c=0
n=1
t=False
while a!='x':
    a=input()
    if a=='x':
        if t:
            list.append(str(b))
            i+=1
        for g in range(0,i):
            print(list[g])
        break
    else:
        if a!=("+" or "-" or "*" or "/" or "%" or "!" or "x") and not(t):
            b=int(a)
            t=True
        if a=='+' and t:
            c=int(input())
            list.append(str(b+c))
            t=False
            i+=1
        elif a=='-' and t:
            c=int(input())
            list.append(str(b-c))
            t=False
            i+=1
        elif a=='*' and t:
            c=int(input())
            list.append(str(b*c))
            t=False
            i+=1
        elif a=='/' and t:
            c=int(input())
            if c!=0:
                list.append(str(b//c))#почему-то делает неправильный вывод при 100/9(если там уже есть какие-то числа), но в пустой лист записывает правильный ответ
                t=False
                i+=1
        elif a=='%' and t:
            c=int(input())
            if c!=0:
                list.append(str(b/c))
                t=False
                i+=1
        elif a=='!' and b>0:
            for m in range(1,b+1):
                n*=m
            list.append(str(n))
            t=False
            i+=1
'''
#7.10
n=-1
a=int(input())
buy=sell=0
t=j=True
while n!=0:
    n=int(input())
    if n>a and t and j:
        buy=n
        t=False
    if n<a and not(t) and j:
        sell=n
        j=False
    a=n
print("\n")
print("================")
print("Купили:",buy," Продали:",sell," Разница:",sell-buy)
