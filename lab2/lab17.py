'''
#17.2
dct = {}
for _ in range(int(input())):
    val, key = input().split()
    if key in dct:
        dct [key].append(val)
    else:
        dct [key] = [val]

for _ in range(int(input())):
    key = input()
    if key in dct:
        print(*dct [key])
    else:
        print('Нет в телефонной книге')
'''

'''
#17.3
sp = {}
n = int(input())
for i in range(n):
    name = input().split()
    if name[2] in sp:
        sp[name[2]].append([name[0], name[1]])
    else:
        sp[name[2]] = [[name[0], name[1]]]

num = int(input())
arr = [input() for _ in range(num)]

for word in arr:
    if word in sp:
        arr = sorted(sp[word], key=lambda x: int(x[1]))
        st = ''
        for x in arr:
            st += ' '.join(x) + ' '
        print(st.rstrip())
    if word not in sp:
        print()
'''


#17.4
n = int(input())
s = input()
time = 0
public,like = s.split(' опубликовал пост, количество просмотров: ')
d = {public:[int(like),'root',time]}
for i in range(1,n):
    s = input()
    time += 1
    if ' отрепостил пост у ' in s:
        repost,s = s.split(' отрепостил пост у ')

        if ', количество просмотров: ' in s:
            autor,like = s.split(', количество просмотров: ')
            like = int(like)
            d[repost] = [like,autor,time]
            while autor != 'root':
                d[autor][0] += like
                autor = d[autor][1]
    elif 'количество просмотров: ' in s:
        s,like = s.split('количество просмотров: ')
        d[public][0] += int(like)
for x in sorted(d,key = lambda y: d[y][2]):
    print(d[x][0])
