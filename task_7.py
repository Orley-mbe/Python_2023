#Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.
#После загрузки задания, вы можете проверить себя самостоятельно с помощью эталонного решения
n = int(input("Введите число n "))
k = 0
count = []
while n >= 1 :
    count.append(pow(2,k))
    n //= 2
    k += 1
print(count)
    
           
    
