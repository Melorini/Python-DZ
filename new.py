"""
Задача 2: Найдите сумму цифр трехзначного числа.
*Пример:*
123 -> 6 (1 + 2 + 3)
100 -> 1 (1 + 0 + 0) |
"""
"""
print("Введите трехзначное число:")
a = int(input())
print('Cумма цифр в числе:', (a//100) + ((a%100)//10) + ((a%100)%10))
"""
"""
Задача 4: Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали S журавликов. Сколько журавликов сделал каждый ребенок, если известно, что Петя и Сережа сделали одинаковое количество журавликов, а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?
*Пример:*
6 -> 1  4  1
24 -> 4  16  4
60 -> 10  40  10
"""
"""
print("Сколько всего журавликов сделали дети:")
s = int(input())
print('Петя и Сережа сделали по - ', s//6, ', Kатя сделала - ', (s//6)*4)
"""
"""
Задача 6: Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и получали билет с номером. Счастливым билетом называют такой билет с шестизначным номером, где сумма первых трех цифр равна сумме последних трех. Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется написать программу, которая проверяет счастливость билета.
*Пример:*
385916 -> yes
123456 -> no
"""
"""
print("Введите шестизначный номер билета:")
a = int(input())
if (((a//100000)+((a%100000)//10000)+(((a%100000)%10000)//1000) == (((((a%100000)%10000)%1000))//100)+((((((a%100000)%10000)%1000))%100)//10)+((((((a%100000)%10000)%1000))%100)%10))) : print("Билет счастливый")
else : print("Билет обычный")
"""
"""
Задача 8: Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек, если разрешается сделать один разлом по прямой между дольками (то есть разломить шоколадку на два прямоугольника).
*Пример:*
3 2 4 -> yes
3 2 1 -> no
"""
n = int(input('Введите длину: '))
m = int(input('Введите ширину: '))
k = int(input('Введите количество долек: '))
if k%n == 0 or k%m == 0: print('Да')
else: print('Нет')
