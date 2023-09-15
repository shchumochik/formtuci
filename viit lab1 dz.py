import time
import math


print('Программа по вычислению корня квадратного уравнения')
print('ax^2 + bx + c = s')


a = float(input('Введите переменную а: '))
b = float(input('Введите переменную b: '))
c = float(input('Введите переменную c: '))
s = float(input('Введите переменную s: '))

if s > 0:
  c = c - s
  s = s - s
if s < 0:
  c = c + s
  s = s - s

D = b**2 - 4 * a * c
print('Считаем дискриминант...')
time.sleep(1)
print('D =', D)


if D > 0:
  x1 = ((-(b) + math.sqrt(D)) / (2 * a))
  x2 = ((-(b) - math.sqrt(D)) / (2 * a))
  print('Считаем первый...')
  time.sleep(1)
  print('Считаем второй корень...')
  time.sleep(1)
  print('x1 =', x1, ' x2 =', x2)

if D == 0:
  x3 = ((-(b)) / (a * 2))
  print('Считаем корень...')
  time.sleep(2)
  print('x =', x3)

if D < 0:
  print('Увы, но решений нет :(')