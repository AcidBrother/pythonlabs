'''
#11.1
message = input()
counter = 1
max = 0
for i in range (len(message)):

    if counter > max:
        max = counter
print(max)

'''

'''
#11.2
n = int(input())
i = 0
list = []
while i < n:
    s = input().replace('%%', '')
    if s.find('####') != -1:
        s = ''
    else:
        list.append(s)
    i += 1
for x in list:
    print(x)
'''

'''
#11.3
message = input()
fav_digit = int(input())
fav_letter = input()
if fav_digit > len(message):
    print('ОШИБКА')
elif len(fav_letter) > 1:
    print('ОШИБКА')
else:
    if message[fav_digit - 1] == fav_letter:
        print('ДА')
    else:
        print('НЕТ')

'''

#11.5
message = input()
i = 0
for i in range(int(len(message))):
    print(message[i: -i])
    i += 1
