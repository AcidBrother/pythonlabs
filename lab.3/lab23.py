'''
#23.2
def find_farthest_orbit(list_of_orbits):
    list = []
    for i in list_of_orbits:
        if i[0] != i[1]:
            list.append(i[0] * i[1])
    far = list.index(max(list))
    return list_of_orbits[far]
'''

'''
#23.3
def pam_param():
    text = input()
    vowel = ['а', 'о', 'э', 'е', 'и', 'ы', 'у', 'ё', 'ю', 'я']
    pam = text.split()
    rhymes = [0] * len(pam)
    for i in range(len(pam)):
        for x in pam[i]:
            if x in vowel:
                rhymes[i] += 1
    if len(set(rhymes)) == 1:
        print("Парам пам-пам")
    else:
        print("Пам парам")
'''

'''
#23.4
import math

def drange(start, stop, step):
    r = start
    while r < stop:
        yield r
        r += step


def distance(t):
    return math.hypot(0.75 - t[0], 0 - t[1])


coords = [(math.cos(3 * t), math.sin(3 * t)) for t in drange(0, 2 * 3.14, 0.1)]

dists = [round(distance(x), 4) for x in coords]

print(min(dists))
'''
