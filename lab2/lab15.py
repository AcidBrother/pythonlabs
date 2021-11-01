'''
#15.2
a=input()
c=0
for b in a:
    if b != ' ' and b !='\t':
        c+=1
print(c)
'''

'''
#15.3
a = input()
n = 0
for i in range(len(s)):
    if s.count(s[i]) > n:
        n = s.count(s[i])
print(n)
'''


#15.5
queue = []
for i in range(int(input())):
    text = input()
    list_text = text.split()
    lower_case = text.lower()
    if 'встал' in lower_case:
        queue.append(list_text[0])
    elif 'будет' in lower_case:
        person, nev_person = list_text[1:3]
        queue.insert(queue.index(person)+1,nev_person)
    else:
        queue.remove(list_text[0])

print(*queue,sep = '\n')
