'''
#14.1
n = int(input())
a = []
for i in range(n):
    f = input()
    if 'лук' in f:
        continue
    a.append(f)
print(', '.join(a))
'''
"""
#14.3
a=input()
print(*a.split(), sep = '\n')
"""


#14.5
import re
print(re.search('text=(\w+)&',input())[1])
