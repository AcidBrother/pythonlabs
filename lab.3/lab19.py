'''
#19.1
ru_mon = ["январь", "февраль", "март", "апрель", "май", "июнь", "июль","август", "сентярбь", "октябрь", "ноябрь", "декабрь"]
en_mon = ["january", "february", "march", "april", "may", "june", "july", "august", "september", "october", "november", "december"]

def month_name(num, lang):
    if lang == "ru":
        print(ru_mon[num-1])
    elif lang == "en":
        print(en_mon[num-1])
'''


'''
#19.2
def t2c(f):
    a=f[:1]
    b=f[1:]
    r=int(b)
    c='ABCDEFGH'.find(a)+1
    return (c,r)

def c2t(k):
    (c,r)=k
    return 'ABCDEFGH'[c-1]+str(r)

def possible_turns(cell):
    (c,r)=t2c(cell)
    tmp=[]
    tmp.append((c+2,r+1))
    tmp.append((c+2,r-1))
    tmp.append((c-2,r+1))
    tmp.append((c-2,r-1))
    tmp.append((c+1,r+2))
    tmp.append((c-1,r+2))
    tmp.append((c+1,r-2))
    tmp.append((c-1,r-2))
    res=[]
    for ((a,b)) in tmp:
        if (a>0) & (b>0) & (a<=8) & (b<=8):
            res+=[c2t((a,b))]
    return sorted(res)
'''

'''
#19.4
def palindrome(word):
    if word == word[::-1]:
        print("Полиндром")
    else:
        print("Не полиндром")

text = input("ВВедите текст\n")
palindrome(text.lower().replace(" ", ""))
'''

'''
#19.6
def catalan(n):
    c = [0] * (n + 1)
    c[0] = 1
    for k in range(1, n + 1):
        c[k] = sum(c[i] * c[k - i - 1] for i in range(k))
    return c[n]
'''
