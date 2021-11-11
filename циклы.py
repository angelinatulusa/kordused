#купи слона
a=input("Kupi slona! ")
while a.title()!="Slon":
    a=input("Vse govorat " +a+ ", a ti kupi! ")
print("Slon tvoi!")



#7. Вывести на экран числа, кратные К из промежутка [А,В].
k=int(input("Kirjutage number: "))




print()
print()
print()
#6. С клавиатуры вводятся N чисел. Составьте программу, которая определяет количество отрицательных,количество положительных и количество нулей среди введенных чисел.Значение N вводится с клавиатуры.
from random import *
n=int(input("Mitu: "))
p=n=o=0
while n>0:
    n-=1
    b=randint(-100,100)
    print(b)
    if b>0:
        p+=1
    elif b<0:
        n+=1
    else:
        o+=1
print("Pos: ",p)
print("Neg: ",n)
print("Nullid: ",o)



print()
print()
print()
#4. Составьте программу, выводящую на экран квадраты чисел от 10 до 20.
for arv in range(10,21,1):
    print(arv**2)


print()
print()
print()
#3. Вводят 8 чисел. Найти их произведение (только положительных).
from random import *
korrutis=1
for i in range(8):
    b=randint(-100,100)
    print(b)
    if b>0: korrutis*=b
print("Korrutis on ",korrutis)




print()
print()
print()
#2. Запросите у пользователя число А и найдите сумму всех натуральных чисел от 1 до А.
a=10
s=0
for arv in range(1,a+1):
    s+=arv
print("Summa: ",s)




#1. FOR
t=0
q=0
for t in range(15):
    a=float(input("Sisesta arv: "))
    if a==round(a): q+=1
print("Taisarvude kogus: ",q)

#1. WHILE
t=0 #kol-vo cisel
q=0 #kol-vo int cisel
while t<15:
    t+=1
    a=float(input("Sisesta arv: "))
    if a==round(a): q+=1
print("Taisarvude kogus: ",q)




print("FOR".center(60,"#"))
for i in range(5):
    print("Hello world!")
print("WHILE TRUE".center(60,"#"))
k=0
while True:
    k+=1
    print("Hello world!")
    if k==5: break
print("WHILE TINGIMUSEGA".center(60,"#"))
k=0
while k<5:
    print("Hello world!")
    k+=1