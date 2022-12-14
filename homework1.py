# 1) Поработайте с переменными, создайте несколько, выведите на экран, 
# запросите у пользователя несколько чисел и строк и сохраните в переменные, выведите на экран.

num = 5
f = 3.56
colors = ['blue','yellow','orange']
print(num, f, colors)

a = int(input('Введите первое число:'))
b = int(input('Введите второе число:'))
print(a, '+' ,b, '=',a + b)

first_name = input('Введите имя 1:')
second_name = input('Введите имя 2:')
print(first_name, second_name)
print()

# 2) Пользователь вводит время в секундах. Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс. 
# Используйте форматирование строк.

time = int(input('Введите время в секундах:'))
hours = time // 60 // 60
if hours > 0:
    minutes = (time // 60) - (hours * 60)
else:
    minutes = time // 60
seconds = time % 60
print(f'{hours} : {minutes} : {seconds}')
print()

# 3) Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn. Например, пользователь ввёл число 3. 
# Считаем 3 + 33 + 333 = 369.

n = int(input('Введите число от 1 до 9:'))
sum = n + (n * 10 + n) + (n * 100 + n * 10 + n)
print(sum)
print()

# 4) Пользователь вводит целое положительное число. Найдите самую большую цифру в числе.
# Для решения используйте цикл while и арифметические операции.

num = int(input('Введите положительное число:'))
max_number = num % 10
while num > 0:
    num = num // 10
    if num % 10 > max_number:
        max_number = num % 10
print('Самая большая цифра в числе = ',max_number)  
print()      

# 5) Запросите у пользователя значения выручки и издержек фирмы. Определите, с каким финансовым результатом работает фирма 
# (прибыль — выручка больше издержек, или убыток — издержки больше выручки). Выведите соответствующее сообщение.
# Если фирма отработала с прибылью, вычислите рентабельность выручки (соотношение прибыли к выручке). 
# Далее запросите численность сотрудников фирмы и определите прибыль фирмы в расчете на одного сотрудника.

revenue = int(input('Введите выручку фирмы:'))
expenses = int(input('Введите издержки фирмы:'))
if revenue > expenses:
    print('Фирма прибыльная')
    profitability = round((revenue - expenses) / revenue, 3)
    print('Рентабельность выручки =',profitability)
    staff = int(input('Введите количество сотрудников фирмы:'))
    profit_staff = round((revenue - expenses) / staff, 3)
    print('Прибыль фирмы в расчете на одного сотрудника = ',profit_staff)
else:
    print('Фирма убыточная')
print()


# 6)Спортсмен занимается ежедневными пробежками. В первый день его результат составил a километров. 
# Каждый день спортсмен увеличивал результат на 10 % относительно предыдущего. 
# Требуется определить номер дня, на который результат спортсмена составит не менее b километров.
# Программа должна принимать значения параметров a и b и выводить одно натуральное число — номер дня.
# Например: a = 2, b = 3.
# Результат:
# 1-й день: 2
# 2-й день: 2,2
# 3-й день: 2,42
# 4-й день: 2,66
# 5-й день: 2,93
# 6-й день: 3,22
# Ответ: на 6-й день спортсмен достиг результата — не менее 3 км.

a = int(input('Введите кол-во км в 1 день:'))
b = int(input('Введите кол-во км b:'))
day = 1
while a < b:
    a = (a / 10) + a 
    day = day + 1
else:
    print(f'На {day} день спортсмен достиг {b} км')
print()


# Дополнительные:
# 1. Напишите программу, которая принимает на вход цифру, обозначающую день недели,
# и проверяет, является ли этот день выходным.
    
number = int(input("Введите номер для недели:"))
if number == 6 or number == 7:
    print('Урра выходной!')
elif number < 1 or number > 7:
    print('Это вообще не номер дня недели')
else: 
    print('Будний день')