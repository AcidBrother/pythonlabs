'''
#18.1
def print_shrug_smile():
    print('¯\\_(ツ)_/¯')

def print_ktulhu_smile():
    print('{:€')

def print_happy_smile():
    print('(͡° ͜ʖ ͡°)')
'''

'''
#18.2
t=False
i=0
b=""
def ask_password():
    pas=input()
    global t
    if pas=='password' and not(t):
        t=True
        b="Пароль принят"
        return b
    elif i>=3 and not(t):
        t=True
        b="В доступе отказано"
        return b
    else:
        t=False
        return ""
while i>=0:
    b=ask_password()
    i+=1
    if t:
        print(b)
'''

'''
#18.3
f1=1
f2=1
t=True
g=0.0
i=0
def golden_ratio(i):
    j=0
    f1=1
    f2=1
    while j<i-2:
        f3 = f1 + f2
        f1=f2
        f2=f3
        j+=1
    g=f2/f1
    print(f2/f1)
    print('444444444444')
    return g
while t:
    i=int(input())
    g=golden_ratio(i)
    print(g)
    print('=======')
'''


#18.4

'''
g=''
def bracket_check(test_string):
    i=0
    a=b=0
    for c in test_string:
        if c=='(':
            a+=1
        elif c==')':
            b+=1
    if a==b:
        g="YES"
        return g
    else:
        g="NO"
        return g
'''
#'''
g=''
def bracket_check(test_string):
    i=j=0
    a=b=0
    for c in test_string:
        i+=1
        if c=='(':
            for v in test_string[i:]:
                j+=1
                if v==')':
                    test_string= test_string[:i-1]+test_string[i:i+j-1]+test_string[i+j:]
                    break
    print(test_string)
    '''if
        g="YES"
        return g
    else:
        g="NO"
        return g
        '''
test_string=input()
k=len(test_string)
g=bracket_check(test_string)
print(g)

'''
#18.5
def equation(a,b):
    x1, y1, x2, y2 = map(float, (a + ";" + b).replace(',', '.').split(';'))
    if x1 == x2:
        print(x1)
    elif y1 == y2:
            print(y1)
    else:
        k = (y2 - y1)  /  (x2 - x1)
        print(k, y2 - k * x2)
'''

'''
#18.6
def line(s,t):
    k, b = map(float, s.replace('x', ' ').split(' '))
    x, y = map(float, (t).split(';'))
    if y == k * x + b:
        print("True")
    else:
        print("False")

'''
