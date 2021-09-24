'''
#4.1
a = ""
b = 0
while a != "Спасибо.":
    a = input()
    b=b+1
print(b)
'''


'''
#4.2
def toFixed(numObj, digits=0):
    return f"{numObj:.{digits}f}"
a = 1
b = 0
c = 0
while a >= -300:
    a = float(input())
    if a>-300:
        c =c+a
        b=b+1

print(toFixed((c/b), 1))
'''

'''
#4.3
a= int(input())
b = 1
c=0
while b<a:
    b*=2
    c+=1
if b==a:
    print(c)
else:print("НЕТ")
'''

'''
#4.4
a=input()
t=True
if int(len(a))<8:
    print("Короткий!")
else:
    i=0
    for i in range(int(len(a))):
        if a[i]=="1" and a[i+1]=="2" and a[i+2]=="3":
            print("Простой!")
            t=False
            break
    if t:
        b=input()
        if a != b:
            print("Различаются.")
        else:print("OK")
'''

'''
#4.5
a = int(input())
n=0
while a != 1:
    if a%2==0:
        a/=2
        n+=1
    else:
        a=3*a+1
        n+=1
print(n)
'''

'''
#4.6
a = 10
while a%10==0:
    a = int(input())
    if a%10!=0:
        break
'''
'''
#4.7
x = int(input())
y = int(input())
'''
'''
#4.8
a=1
b=1000
t=True
c=0
while c<11 and t:
    if a !=1:
        print(a+b//4)
    else:
        print(b//2)
    d=input()
    if d=="<":
        a=b//2
        c+=1
    elif d==">":
        b=b//2
        c+=1
    elif d=="=":
        break
'''
