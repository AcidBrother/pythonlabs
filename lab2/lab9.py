"""
#9.1
library = int(input())
task = int(input())
books = []
i = 0
while i < library:
    books.append(input())
    i += 1
i = 0
while i < task:
    taskbooks = input()
    if taskbooks in books:
        print('YES')
    else: print('NO')
    i += 1
"""

"""
#9.2
lessons = int(input())
attend = []
all = []
i = j = 0
while i < lessons:
    pupils = int(input())
    while j < pupils:
        student = input()
        attend.append(student)
        j += 1
        if attend.count(student) == lessons:
            all.append(student)
    j = 0
    i += 1
for x in all:
    print(x)
"""

"""
#9.3
amount = int(input())
surnames = []
i = 0
sakes = 0
while i < amount:
    man = input()
    surnames.append(man)
    i += 1
sakes = {i: surnames.count(i) for i in surnames}
print(sakes)
"""

"""
#9.4
m = int(input())
ingredients = []
i = j = k = 0
while i < m:
    ingredients.append(input())
    i += 1
n = int(input())
while j < n:
    recipe = input()
    m = int(input())
    while k < m:
        ingredient = input()
        if ingredient in ingredients == m:
            print(recipe)
        k += 1
    j += 1
 """

#9.5
m = int(input())
dishes = []
i = j = k = 0
while i < m:
    dishes.append(input())
    i += 1
n = int(input())
while j < n:
    m = int(input())
    while k < m:
        used = input()
        if used in dishes:
            dishes.remove(used)
        k += 1
    j += 1
for x in dishes:
    print(x)
 
