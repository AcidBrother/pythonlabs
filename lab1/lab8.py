'''
#8.1
ii=int(input())
jj=int(input())
for j in range(1, jj+1):
    print(*(i/j for i in range(1, ii+1)), sep=' ')
'''

'''
#8.2
a=int(input())
b=int(input())
c=input()
print(c*b)
for n in range(a-2):
   print(c+' '*(b-2)+c)
print(c*b)
'''

#8.3
a=int(input())
b=int(input())
for n in range(1,a//20):
    for d in range(0,a//10):
        for e in range(0,a//5):
            if((n*20+d*10+e*5)==a)and(n+d+e==b):
                print(n,' ',d,' ',e)
