'''
#10.1
word = input()
index = int(input())
if 0 < index <= len(word):
    print(word[index-1].capitalize())
else:
    print('ОШИБКА')
'''

'''
#10.2
position = int(input())
message = input().upper()
for i in message:
    pos = alphabet.find(i)
'''

'''
#10.3
message = input().lower()
if message[0] == 'а':
    print('ДА')
else:
    print('НЕТ')
'''

'''
#10.4
message = input()
print(message[-1])
'''

'''
#10.5
message = 'а'
while message[0].lower() == 'а':
    message = input()
'''


#10.6
trail = input()
a = trail[1::].replace('V', '!V!').split('!')
current_pos = 0
k = 1 if len(trail) == 1 or trail[1] == 'V' else 0
for i in a:
    if i == '':
        continue
    elif i[0] == '<':
        current_pos -= len(i)
        print(current_pos * ' ' + trail[0]  + i.replace('<', trail[0]))
        k = 0
    elif i[0] == '>':
        print(current_pos * ' ' + trail[0]  + i.replace('>', trail[0]))
        current_pos += len(i)
        k = 0
    elif i[0] == 'V':
        if k :
            print(current_pos * ' ' + trail[0])
        k = 1
if k :
    print(current_pos * ' ' + trail[0])
