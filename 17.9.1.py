numbers_string=input('Введите числа через пробел:')
#преобразование веденной последовательности в список
numbers_list=numbers_string.split()
print(f'Список введенных чисел:{numbers_list}')
#сортировка по возрастанию
def sort_up(lst):
    return sorted(lst)
#алгоритм двоичного поиска
def binary_search(array, element, left, right):
#ищем середину
    middle = (left + right) // 2

#все числа одинаковые
    if array[left] == array[right] == element:
        return 'любым'

#число больше последнего в списке или равно ему
    if element >= array[right]:
        return '[' + str(right + 1) + '] после ' + str(array[right])

#число меньше первого в списке или равно ему
    if element <= array[left]:
        return '[' + str(left) + '] перед ' + str(array[left])

#число равно среднему
    if array[middle] == element:
        return '[' + str(middle + 1) + '] между ' + str(array[middle]) + ' и ' + str(array[middle + 1])

#число меньше среднего
    elif element < array[middle]:
        return binary_search(array, element, left, middle - 1)

#число больше среднего
    elif element > array[middle]:
        return binary_search(array, element, middle + 1, right)
#новый список с преобразованием в числа
numbers=[]
for i, item in enumerate(numbers_list):
    numbers_list[i] = int(item)
    numbers.append(item)
numbers=sort_up(numbers_list)
print(f'Введенные числа в порядке возрастания: {numbers}')
some_num=int(input('Введите любое число:'))
# установление позиции нового числа в списке
pos = binary_search(numbers, some_num, 0, len(numbers) - 1)
print(f'Введенное число будет на позиции: {pos}')
#добавление числа в список
numbers.append(some_num)
numbers=sort_up(numbers)
print(f' Обновленный список: {numbers}')