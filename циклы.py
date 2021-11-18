#5. Составьте программу для вычисления площади трапеции.
t=int(input("ho4es naiti plosad trapecii?(da-1) ")) 
if t==1:
    a=0.0
    while a<=0:
        try:
            a=int(input("cemu ravna storona a? "))
        except ValueError:
            print("tolko cisla bolse cem 0")
    b=0.0
    while b<=0:
        try:
            b=int(input("cemu ravna storona b? "))
        except ValueError:
            print("tolko cisla bolse cem 0")
    h=0.0
    while h<=0:
        try:
            h=int(input("cemu ravna visota h? "))
        except ValueError:
            print("tolko cisla bolse cem 0")
    S=0.5*(a+b)*h
    print("plosad ravna - ",S)
    q=input("hotes ese? ")
    if q!="da": quit()
else:
    print("horoso, dosvidania!")


print()
print()
print()
#primer
from keyboard import *
while True:
    print("Hello!")
    if is_pressed("esc"): break


print()
print()
print()
#28. Реализуйте "мини лотерею". Пусть компрьютер "задумает число", а пользователь его должен отгадать. В конце сообщив количество попыток.
from random import *
b=randint(1,10)
a=int(input("Kakoe cislo? "))
for b in range(1,10):
    if a==b:
        print("Pozdravlau, vi ugadali cislo!")
        break
    else:
        int(input("Neverno, poprobuite ese raz. Kakoe cislo? "))

print()
print()
print()
#4.  Имеется кусок ткани длиной М метров. От него последовательно отрезаются куски разной длины. Все данные по использованию ткани заносятся в компьютер. Компьютер должен выдать сообщение о том, что материала не хватает, если будет затребован кусок ткани, большей длины, чем имеется и предложить выкупить остаток. Если пользователь согласен, то продается последний кусок и программа заканчивает работу, если нет, то переходим к следующиму покупателю.
from random import *
M=randint(10,100)
print("v magazine",M,"m tkani")
while M>0:
    m=int(input("kakoi kusok hotite? "))
    if M>=m:
        M-=m
        print("u nas ostalos",M,"m")
    else:
        print("u nas nehvataet tkani")
        v=input("hotite kupit ostatok? ")
        if v=="da":
            print("tkan vasa")
            M=0
        else:
            print("ne hotes, kak hotes")
print("v magazine zakoncilas tkan",M,"m")
    



print()
print()
print()
#3. Начав тренировки, спортсмен в первый день пробежал 10 км. Каждый день он увеличивал дневную норму на 10% нормы предыдущего дня. Какой суммарный путь пробежит спортсмен за 7 дней?
km=s_pikkus=10 #km v pervii den
print("1. v den put bil ", km)
for d in range(2,8):
    km*=1.1
    print(d,". v den put bil ",round(km,2))
    s_pikkus+=km
    print(d,". v den summarnii put bil ",round(s_pikkus,2))



print()
print()
print()
#1. Определить и вывести максимальное из N вводимых пользователем чисел.
ask_P=ask_N=""
while type(ask_P)!=int:
    try:
        ask_P=int(input("skolko cisel vi hotite vvesti? "))
    except ValueError:
        print("Ainult täisarvud!")
if ask_P>0:
    while type(ask_N)!=int:
        ask_N=int(input("kakoe cislo vvodim?"))
        print(" ")
    ask_P-=1
    maks=ask_N
while ask_P>0:
    ask_N=int(input("kakoe cislo vvodim?"))
    ask_P-=1
if ask_N>maks: 
    maks=ask_N
    print("maksimalnoe cislo eto ", maks)
else:
    print("ne mogu naiti maksimalnoe cislo")

#Задачи по теме IF,While, For и проверка вводимых данных


print()
print()
print()
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