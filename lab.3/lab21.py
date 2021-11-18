'''
#21.1
def from_string_to_list(string, container):
    container.extend(map(int, string.split()))

a = [1, 2, 3]
from_string_to_list("1 3 99 52", a)
print(*a)
a = [77, 'abc']
from_string_to_list("", a)
print(*a)
'''

'''
#21.2
matrix = [[]]
def transpose(matrix):
    res=[]
    n=len(matrix)
    m=len(matrix[0])
    for j in range(m):
        tmp=[]
        for i in range(n):
            tmp=tmp+[matrix[i][j]]
        res=res+[tmp]
    matrix[:] = res
    return matrix
'''

'''.
#21.5
def defractalize(fractal):
  return [x for x in fractal if x is not fractal]

fractal = [2, 5]
fractal.append(fractal)
fractal.append(3)
fractal.append(fractal)
fractal.append(9)
defractalize(fractal)
print(fractal)
'''

'''
#21.6
wb_tree = []
def tree():
    white = []
    black = [white, white, white]
    white.append(black)
    white.append(black)
    wb_tree = black
'''
