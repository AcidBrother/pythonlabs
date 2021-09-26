n=int(input())
t = True
for i in range(0,n):
    a=input()
    if a=="Кот" or a=="кот":
        print("Мяу")
        t=False
        break;
if t:
        print("НЕТ")
