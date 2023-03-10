# Имеется список чисел. Создайте список, в который попадают числа, описывающие максимальную возрастающую последовательность. Порядок элементов менять нельзя.
# Одно число - это не последовательность.

# Пример:

# [1, 5, 2, 3, 4, 6, 1, 7] => [1, 7]
# [1, 5, 2, 3, 4, 1, 7, 8 , 15 , 1 ] => [1, 5]
# [1, 5, 3, 4, 1, 7, 8 , 15 , 1 ] => [3, 5]

# Комментарий: Так как нам нужно искать возрастающую последовательность - для удобства имеет смысл отсортировать список
# В последствии алгоритм оттакливается от конечно индекса элемента наибольшей последовательности и её количества.

import os
os.system('cls')

# Создаем список, сортируем и выводим его в печать
list_base = [1, 5, 3, 4, 1, 7, 8 , 15 , 1 ]
list_base.sort()
print(list_base)

count = 0           # Переменная подсчета количества текущей последовательности
count2 = 0          # Переменная, куда записывается большее количество последовательности
count_i = 0         # Переменная индекса текущей последовательности, от которого идет отсчет назад до индекса её начала
count_i2 = 0        # Переменная индекса болшей последовательности, от которого идет отсчет назад до индекса её начала
# Флажок для отработки условия сравнения последовательности на последнем элементе списка
flag = True

for i in range(len(list_base)):
    if i == 0:
        continue             # По моему алгоритму, сравнение невозможно на первом элементе списка, поэтому его пропускаем

    if i == len(list_base)-1:       # Здесь "опускаем" флажок, на последнем элементе списка
        flag = False

# Далее блок текущей последовательности:
# Сравниваем текущий и предыдущий элемент списка. Если они образуют последовательность то
# записываем индекс элемента и увеличиваем количество текущей последовательнсти.
# При условии, если оцениваем последний элемент списка и он образует текущую последовательность
# а также, если эта последовательность является наибольшей - мы перезаписываем переменные
    if (list_base[i] == list_base[i-1]+1):
        count += 1
        count_i = i
        if (flag == False) and (count > count2):
            count2 = count
            count_i2 = count_i

# Блок, если последовательность прерывается:
# Если получившаяся текущая последовательность кончается, и она является наибольшей из предыдущих
# перезаписываем переменные
    else:
        if count > count2:
            count2 = count
            count_i2 = count_i
            count = 0


# Если итоговая последовательность состоит из 1 числа - то пишем ошибку
if count_i2 - count2 == count_i2:
    print('Одно число это не последовательность!')
else:
    # Иначе выводим значения начала и конца последовательности
    print(f'[{list_base[count_i2 - count2]}, {list_base[count_i2]}]')
