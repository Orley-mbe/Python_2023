#Задача 32: Определить индексы элементов массива (списка), 
#значения которых принадлежат заданному диапазону (т.е. не 
#меньше заданного минимума и не больше заданного
#максимума)
import math
import random

n = int(input('Введите число  '))
list_number = [random.randint(0, n + 1) for el in range(n + 1)]
print(list_number)
minNum = int(input('Введите минимум диапазона '))
maxNum = int(input('Введите максsимум диапазона '))
for el in list_number[minNum:maxNum+1]: 
    print(f'{el},{list_number.index(el, minNum, maxNum)}')

    
#result = [ (i, list_number.index(i, minNum, maxNum)) for i in list_number]
#for el in list_number:
#    result = []
#    if el in range(minNum, maxNum):
#        result.append(enumerate())

