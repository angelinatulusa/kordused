#28. Реализуйте "мини лотерею". Пусть компрьютер "задумает число", а пользователь его должен отгадать. В конце сообщив количество попыток.
from random import *
b=randint(1,10)
a=int(input("Kakoe cislo? "))
for i in range(1,10):
    if a==b:
        print("Pozdravlau, vi ugadali cislo!")
    else:
        int(input("Neverno, poprobuite ese raz. Kakoe cislo? "))



print()
print()
print()
#29. Напишите программу, печатающую столбик строк такого вида
for g in range(0,10):
    print("x")
for j in range(1,10):
    for i in range(1,10):
        if i==j:
            print("x",end=" ")
        else:
           print("0",end=" ")
    print()




print()
print()
print()
#16. Напишите программу, печатающую столбик строк такого вида
for j in range(1,10):
    for i in range(1,10):
        if i==j:
            print(j,end=" ")
        else:
            print("0",end=" ")
    print()



print()
print()
print()
#tablica 
for j in range(1,10):
    for i in range(1,10):
        print(f"{(j*i):2}",end=" ")
    print()



print()
print()
print()
#15. Написать программу, выводящую в столбик десять строк, в каждой печатая цифры от 0 до 9
for j in range(0,10):
    for i in range(0,10):
        print(i,end=" ")
    print(j)



print()
print()
print()
#17. Напишите программу, печатающую столбик таблицу умножения
n=int(input("Kirjutage number: "))
for i in range(1,10):
    print(n,"*",i,"=",n*i)

print()
print()
print()
#купи слона
a=input("Kupi slona! ")
while a.title()!="Slon":
    a=input("Vse govorat " +a+ ", a ti kupi! ")
print("Slon tvoi!")


print()
print()
print()
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