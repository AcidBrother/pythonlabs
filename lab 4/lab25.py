'''
#25.1
from random import sample
import string

symbols = 'ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnpqrstuvwxyz23456789'

def generate_password(m):
    return ''.join(sample(symbols,m))

def main(n, m):
    a = set()
    while len(a) < n:
        a.add(generate_password(m))
    return a

print("Случайный пароль из 7 символов:", generate_password(7))
print("10 случайных паролей длиной 15 символов:")
print(*main(10, 15), sep="\n")
'''

'''
#25.2
import itertools
import random
import string

bad_symbols = '1IlOo0'
uppercase_ = list(filter((lambda x: x not in bad_symbols),string.ascii_uppercase))
lowercase_ = list(filter((lambda x: x not in bad_symbols),string.ascii_lowercase))
digits_ = list(filter((lambda x: x not in bad_symbols),string.digits))

def generate_password(m):

	min_ = 1
	max_ = m-2
	u = random.randint(1,max_)

	max_ = m - u - 1
	d = random.randint(1,max_)

	l = m - u - d

	result = [random.choice(uppercase_) for i in range(u)]
	result += [random.choice(lowercase_) for i in range(l)]
	result += [random.choice(digits_) for i in range(d)]
	random.shuffle(result)
	result = ''.join(result)
	return result

def main(n,m):
	z = set()
	while len(z) < n:
		z.add(generate_password(m))
	return list(z)

#print("Случайный пароль из 7 символов:" , generate_password(7))
print("10 случайных паролей длиной 15 символов:")
print(*main(10, 15), sep="\n")
'''

'''
#25.3
import random

k = 0.0
for i in range(500000):
    x = random.random()
    y = random.random()
    k += (x * x + y * y < 1.0)
print(4 * k / 500000)
'''


'''
#25.4
import random
import string


def generate_password(m):
  x = random.randint(1, m-2)
  y = random.randint(1, m - x - 1)
  z = m - x - y

  l = []

  i = 0
  while i < x:
    n = random.choice(string.digits)
    if n != '1' and n != '0':
      l.append(n)
      i += 1

  i = 0
  while i < y:
    u = random.choice(string.ascii_uppercase)
    if u != 'I' and u != 'O':
      l.append(u)
      i += 1

  i = 0
  while i < z:
    w = random.choice(string.ascii_lowercase)
    if w != 'l' and w != 'o':
      l.append(w)
      i += 1

  random.shuffle(l)
  return ''.join(l)

def main(n, m):
  list_of_passwords = []
  for i in range(n):
    list_of_passwords.append(generate_password(m))
  return list_of_passwords

print("Случайный пароль из 7 символов:" , generate_password(7))
print("10 случайных паролей длиной 15 символов:")
print(*main(10, 15), sep="\n")
'''
